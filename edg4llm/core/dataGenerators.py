import os
from typing import Dict, Any

from edg4llm.utils.logger import custom_logger
from edg4llm.models.chatglm import EDGChatGLM
from edg4llm.models.chatgpt import EDGChatGPT
from edg4llm.models.internlm import EDGInternLM
from edg4llm.models.deepseek import EDGDeepSeek
from edg4llm.text_generators.answer_generator import AnswerGenerator
from edg4llm.text_generators.question_generator import QuestionGenerator
from edg4llm.text_generators.dialogue_generator import DialogueGenerator

logger = custom_logger("dataGenerator")

class DataGenerator:
    def __init__(self, pConfig):
        """
        Initialize the Data Generator

        This method initializes the model and its associated generators (Answer, Question, Dialogue)
        based on the provided configuration parameters.

        Parameters
        ----------
        pConfig : dict
            A configuration dictionary containing the following key-value pairs:
            - "model_provider" : str, optional
                The type of language model to use ("chatglm", "chatgpt", "internlm", "deepseek"). Default is "chatglm".
            - "model_name" : str, optional
                The specific model to use within the selected provider. Default is "chatglm-4-flash".
            - "base_url" : str
                The base URL for the LLM API. Default is None.
            - "api_key" : str
                The API key for authenticating requests. Default is None.

        Raises
        ------
        ValueError
            If the provided model type is not supported, raises a `ValueError`.

        Attributes
        ----------
        model : object
            The selected language model instance, initialized based on the "model_provider" configuration.
        answer_generator : AnswerGenerator
            An instance of the AnswerGenerator to generate answers.
        question_generator : QuestionGenerator
            An instance of the QuestionGenerator to generate questions.
        dialogue_generator : DialogueGenerator
            An instance of the DialogueGenerator to generate dialogues.

        Notes
        -----
        - Supported model providers include: "chatglm", "chatgpt", "internlm", "deepseek".
        - If the "model_provider" is unsupported, a `ValueError` will be raised.
        """
        
        if pConfig["model_provider"] == "chatglm":
            self.model = EDGChatGLM(
                base_url=pConfig["base_url"],
                api_key=pConfig["api_key"]
            )
        elif pConfig["model_provider"] == "chatgpt":
            self.model = EDGChatGPT(
                base_url=pConfig["base_url"],
                api_key=pConfig["api_key"]
            )
        elif pConfig["model_provider"] == "internlm":
            self.model = EDGInternLM(
                base_url=pConfig["base_url"],
                api_key=pConfig["api_key"]
            )
        elif pConfig["model_provider"] == "deepseek":
            self.model = EDGDeepSeek(
                base_url=pConfig["base_url"],
                api_key=pConfig["api_key"]
            )
        else:
            raise ValueError("Unsupported model provider")

        self.answer_generator = AnswerGenerator(self.model)
        self.question_generator = QuestionGenerator(self.model)
        self.dialogue_generator = DialogueGenerator(self.model)


    def generate_question(self, prompt: str) -> str:
        """
        生成问题数据

        :param prompt: 用于生成问题的提示文本
        :return: 生成的问题
        """
        pass

    def generate_answer(self, question: str) -> str:
        """
        生成答案数据
        
        :param question: 用于生成答案的问题
        :return: 生成的答案
        """
        pass

    def generate_dialogue(self, tConfig) -> list[Dict]:
        """
        Generate a dialogue based on the given configuration.

        This method utilizes the `dialogue_generator` to generate dialogues using the
        provided configuration options. It supports various parameters to control
        the text generation process, such as task type, prompts, sampling strategies, and output formatting.

        Parameters
        ----------
        tConfig : dict
            A configuration dictionary containing the following key-value pairs:
            - "task_type" : str, optional
                The type of task for data generation. Must be one of 'question', 'answer', or 'dialogue'. 
                Default is 'dialogue'.
            - "system_prompt" : str, optional
                A system-level prompt to guide the text generation. Default is None.
            - "user_prompt" : str, optional
                A user-provided prompt to initiate the text generation. Default is None.
            - "do_sample" : bool, optional
                Whether to use sampling during text generation. If True, enables sampling strategies like temperature 
                and top_p. If False, uses deterministic decoding. Default is True.
            - "temperature" : float, optional
                Sampling temperature to control randomness. Must be in the range [0.0, 1.0]. 
                Default is 0.95.
            - "top_p" : float, optional
                Nucleus sampling parameter for controlling randomness. Must be in the range [0.0, 1.0]. Default is 0.7.
            - "max_tokens" : int, optional
                The maximum number of tokens to generate in the output. Default is 4095.
            - "num_samples" : int, optional
                The number of output samples to generate. Default is 10.
            - "output_format" : str, optional
                The format of the output. Default is "alpaca".

        Returns
        -------
        list of dict
            A list of dictionaries containing the generated dialogue outputs.

        Notes
        -----
        - This method uses the `generate` method from the `dialogue_generator` to produce dialogue outputs 
          based on the provided configuration.
        - The `tConfig` dictionary allows for flexible generation based on task type, system/user prompts, 
          and various sampling strategies.
        """

        data = self.dialogue_generator.generate(tConfig)
        return data