import os
import sys
import json
from typing import Dict, Any

from edg4llm.utils.logger import custom_logger
from edg4llm.generators.text_generators.base_generator import BaseGenerator

logger = custom_logger("AnswerGenerator")

class AnswerGenerator(BaseGenerator):
    """
    A class for generating answers based on user queries using a specified model.

    This class extends the `BaseGenerator` class and provides functionality to generate
    answers to user queries based on a given configuration. It interacts with the model's 
    `execute_request` method to generate responses based on system-level and user-level prompts. 
    It supports customization through parameters such as temperature, sampling strategies, 
    and token limits.

    Attributes
    ----------
    model : object
        The model interface used for generating answers.

    Methods
    -------
    generate(tConfig: dict) -> list of dict:
        Generates answers based on the provided configuration.

    Notes
    -----
    - The `generate` method ensures valid answers are returned, retrying if necessary.
    - It logs progress for each generated answer.
    """

    def __init__(self, model):
        """
        Initialize the AnswerGenerator.

        Parameters
        ----------
        model : object
            The model interface used for generating answers.
        """

        super().__init__(model)

    def generate(self, tConfig) -> str:
        """
        Generate answers based on the provided configuration.

        This method generates one or more answers based on the parameters provided in 
        the `tConfig` dictionary. It uses the model's `execute_request` method to generate
        answers based on the system and user prompts, with options to control randomness,
        output length, and sampling strategy.

        Parameters
        ----------
        tConfig : dict
            A configuration dictionary containing the following key-value pairs:
            - "system_prompt" : str, optional
                A system-level prompt that provides context for generating the answer. Default is an empty string.
            - "user_prompt" : str
                A user-provided prompt (query) to generate the corresponding answer.
            - "model" : str, optional
                The specific model to use for answer generation. Default is "glm-4-flash".
            - "do_sample" : bool, optional
                Whether to use sampling strategies during answer generation. Default is True.
            - "temperature" : float, optional
                A sampling parameter to control the randomness of the output. Must be between 0.0 and 1.0. Default is 0.95.
            - "top_p" : float, optional
                Nucleus sampling parameter controlling the cumulative probability range for token selection. 
                Must be between 0.0 and 1.0. Default is 0.7.
            - "max_tokens" : int, optional
                The maximum number of tokens to generate in the answer. Default is 4095.
            - "num_samples" : int, optional
                The number of answers to generate. Default is 1.
        
        Returns
        -------
        list of dict
            A list of dictionaries containing the generated answers. Each dictionary 
            includes the generated answer content and relevant metadata.

        Notes
        -----
        - The method will retry generating answers if the model fails to provide a valid response.
        - Progress and debug information are logged for each generated answer.
        """

        # Extract configuration parameters
        system_prompt = tConfig.get("system_prompt", "")
        user_prompt = tConfig.get("user_prompt", "")
        do_sample = tConfig.get("do_sample", True)
        temperature = tConfig.get("temperature", 0.95)
        top_p = tConfig.get("top_p", 0.7)
        max_tokens = tConfig.get("max_tokens", 4095)
        num_samples = tConfig.get("num_samples", 1)  # Default is to generate 1 sample
        question_path = tConfig.get("question_path", None)

        try:
            with open(question_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            if isinstance(data, dict):  # If it's a single dictionary, wrap it in a list
                data = [data]
            elif not isinstance(data, list):  # Ensure it's a list of dictionaries
                raise ValueError("Invalid JSON structure. Expected a list or a dictionary.")

            # Extract questions
            questions = [item["question"] for item in data if "question" in item]
        except FileNotFoundError:
            logger.error("The file at path %s was not found.", question_path)
            return None
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON from file %s: %s", question_path, str(e))
            return None
        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            return None

        if len(questions) != num_samples:
            logger.error(
                "The number of questions (%d) does not match the expected number (%d). Please check your input.",
                len(questions),
                num_samples,
            )

            sys.exit(1)  # 非零退出码表示异常终止

        # List to store the generated dialogues
        dialogues = []

        # Generate dialogues for the specified number of samples
        total_samples = num_samples  # Total number of samples to generate
        logger.info("Starting the data generation process.")
        for _idx, question in enumerate(questions):
            retry_count = 0  # 初始化重试计数
            max_retries = 5  # 设置最大重试次数（根据需要调整）

            while True:  # Keep trying until valid dialogue data is generated
                retry_count += 1

                generated_answer = self.model.execute_request(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt.replace("EDG4LLM", question),
                    do_sample=do_sample,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                )

                if "error" in generated_answer:
                    logger.warning(
                        "Sample %d: Request failed with error: %s. Retrying (%d/%d)...",
                        _idx + 1,
                        generated_answer["error"],
                        retry_count,
                        max_retries,
                    )
                    
                    if retry_count >= max_retries:
                        logger.error("Sample %d: Max retries reached. Skipping this sample.", _idx + 1)
                        break  # 跳出当前样本，进入下一个
                    continue  # 继续当前样本的生成

                # Convert the generated dialogue to the desired format (e.g., Alpaca format)
                converted_generated_answer = self._convert_original_to_alpaca_answer(system_prompt, question, generated_answer)

                if converted_generated_answer is not None:
                    # If the dialogue is valid, append it to the results and break the loop
                    dialogues.append(converted_generated_answer)
                    break
                else:
                    logger.warning(
                        "Sample %d: Generated answer is None. Retrying (%d/%d)...",
                        _idx + 1,
                        retry_count,
                        max_retries,
                    )
                    
                    if retry_count >= max_retries:
                        logger.error("Sample %d: Max retries reached. Skipping this sample.", _idx + 1)
                        break  # 跳出当前样本

            # Log the progress of dialogue generation
            progress = ((_idx+1) / total_samples) * 100
            logger.info("Data generation progress: %.2f%% (%d/%d samples completed)", progress, _idx+1, total_samples)

        return dialogues
