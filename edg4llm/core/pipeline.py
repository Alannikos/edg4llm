import os

from edg4llm.utils.logger import custom_logger
from edg4llm.core.dataGenerators import DataGenerator
from edg4llm.core.processor import DataProcessor

logger = custom_logger("pipeline", "INFO")

class Pipeline:
    def __init__(self, model_type: str, api_key: str):
        """
        初始化数据生成流程
        :param model_type: 使用的模型类型（如 openai）
        :param api_key: 用于身份验证的 API 密钥
        """
        self.data_generator = DataGenerator(model_type, api_key)
        self.processor = DataProcessor()  # 用于数据后处理

    def generate_data(self, prompt: str, data_type: str) -> dict:
        """
        根据提示生成微调数据

        :param prompt: 输入的提示文本
        :param data_type: 数据类型（如 'question', 'answer', 'dialogue'）
        :return: 微调数据
        """
        if data_type == "question":
            data = self.data_generator.generate_question(prompt)
        elif data_type == "answer":
            data = self.data_generator.generate_answer(prompt)
        elif data_type == "dialogue":
            data = self.data_generator.generate_dialogue(prompt)
        else:
            raise ValueError("Unsupported data type")

        # 对生成的数据进行后处理
        return self.processor.process(data)
