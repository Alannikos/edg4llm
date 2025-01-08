import os

from edg4llm.utils.logger import custom_logger
from edg4llm.models.chatglm import EDGChatGLM
from edg4llm.text_generators.answer_generator import AnswerGenerator
from edg4llm.text_generators.question_generator import QuestionGenerator
from edg4llm.text_generators.dialogue_generator import DialogueGenerator


class DataGenerator:
    def __init__(self, pConfig):
        """
        初始化数据生成器
        
        :param model_type: 使用的模型类型（例如：openai）
        :param api_key: 用于身份验证的 API 密钥
        """

        if pConfig["model_type"] == "chatglm":
            self.model = EDGChatGLM(
                base_url=pConfig["base_url"]
                , api_key=pConfig["api_key"]
                )  # 根据模型类型选择不同的模型
        else:
            raise ValueError("Unsupported model type")

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

    def generate_dialogue(self, tConfig) -> list:

        data = self.dialogue_generator.generate(tConfig)
        return data