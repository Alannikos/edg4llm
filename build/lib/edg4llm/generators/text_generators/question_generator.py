import os
from typing import Dict, List, Any
from edg4llm.utils.logger import custom_logger
from edg4llm.generators.text_generators.base_generator import BaseGenerator

logger = custom_logger("QuestionGenerator")

class QuestionGenerator(BaseGenerator):
    """
    A class for generating questions based on user prompts and configuration.

    This class extends the `BaseGenerator` class and provides functionality to generate
    questions using a specified model. It interacts with the model's `execute_request` 
    method to create output based on user-defined parameters such as sampling strategies,
    temperature, and maximum tokens.

    Attributes
    ----------
    model : object
        The model interface used for generating questions.

    Methods
    -------
    generate(tConfig: dict) -> list of dict:
        Generates questions based on the provided configuration.

    Notes
    -----
    - The `generate` method ensures valid responses are returned, retrying if necessary.
    - Logs progress for each generated question.
    """

    def __init__(self, model):
        """
        Initialize the QuestionGenerator.

        Parameters
        ----------
        model : object
            The model interface used for generating questions.
        """
        
        super().__init__(model)

    def generate(self, tConfig: Dict) -> List:
        """
        Generate questions based on the provided configuration.

        This method generates one or more questions using the parameters specified 
        in the `tConfig` dictionary. It interacts with the model's `execute_request` 
        method to generate output based on user prompts and various sampling options.

        Parameters
        ----------
        tConfig : dict
            A dictionary containing configuration options for question generation:
            - "system_prompt" : str, optional
                A system-level instruction to guide the question generation. Default is an empty string.
            - "user_prompt" : str, optional
                A user-provided input to guide the question generation. Default is an empty string.
            - "model" : str, optional
                Specifies the model for text generation. Default is "glm-4-flash".
            - "do_sample" : bool, optional
                Whether to use sampling during generation. Default is True.
            - "temperature" : float, optional
                Controls randomness in output. Value should be between 0.0 and 1.0. Default is 0.95.
            - "top_p" : float, optional
                Nucleus sampling parameter to limit token selection to a cumulative probability. Default is 0.7.
            - "max_tokens" : int, optional
                The maximum number of tokens for the output. Default is 4095.
            - "num_samples" : int, optional
                The number of question samples to generate. Default is 1.

        Returns
        -------
        list of dict
            A list of dictionaries containing the generated questions.

        Notes
        -----
        - The method retries generation until a valid response is obtained.
        - Logs progress for each generated sample.
        """

        # Extract parameters from the configuration
        system_prompt = tConfig.get("system_prompt", "")
        user_prompt = tConfig.get("user_prompt", "")
        do_sample = tConfig.get("do_sample", True)
        temperature = tConfig.get("temperature", 0.95)
        top_p = tConfig.get("top_p", 0.7)
        max_tokens = tConfig.get("max_tokens", 4095)
        num_samples = tConfig.get("num_samples", 1)

        # Initialize a list to store generated questions
        questions = []
        cur_len = 0
        # Generate questions for the specified number of samples
        logger.info("Starting the data generation process.")
        for _idx in range(1, num_samples + 1):
            retry_count = 0  # 初始化重试计数
            max_retries = 5  # 设置最大重试次数（根据需要调整）

            while True:  # Retry until a valid question is generated
                retry_count += 1

                generated_question = self.model.execute_request(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    do_sample=do_sample,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                )

                if "error" in generated_question:
                    logger.warning(
                        "Sample %d: Request failed with error: %s. Retrying (%d/%d)...",
                        _idx,
                        generated_question["error"],
                        retry_count,
                        max_retries,
                    )

                    if (retry_count >= max_retries):
                        logger.error("Sample %d: Max retries reached. Skipping this sample.", _idx)
                        break  # 跳出当前样本

                # Convert the raw output to a specific format
                converted_question = self._convert_original_to_json(generated_question)

                if converted_question is not None:
                    cur_len = len(converted_question)
                    questions.extend(converted_question)
                    break
                else:
                    logger.warning(
                        "Sample %d: Generated dialogue is None. Retrying (%d/%d)...",
                        _idx,
                        retry_count,
                        max_retries,
                    )
                    
                    if retry_count >= max_retries:
                        logger.error("Sample %d: Max retries reached. Skipping this sample.", _idx)
                        break  # 跳出当前样本

            # Log progress for tracking generation completion
            progress = (_idx / num_samples) * 100
            logger.info("Generation progress: %.2f%% (%d samples generated, %d/%d epoch completed)", progress, cur_len, _idx, num_samples)

        return questions
