import os

from edg4llm.utils.logger import custom_logger
from edg4llm.core.dataGenerators import DataGenerator

logger = custom_logger("DataPipeline", "INFO")


"""
        self._pConfig = {
            "model_type" : model_type
            , "api_key" : api_key
            , "do_sample" : do_sample
            , "temperature" : temperature
            , "top_p" : top_p
            , "max_tokens" : max_tokens
        }
"""

class DataPipeline:
    def __init__(self, pConfig):
        """
        初始化数据生成流程
        :param model_type: 使用的模型类型（如 openai）
        :param api_key: 用于身份验证的 API 密钥
        """
        self.data_generator = DataGenerator(pConfig)

    def generate_data(self, tConfig) -> dict:
        """
        根据提示生成微调数据

        :param prompt: 输入的提示文本
        :param data_type: 数据类型（如 'question', 'answer', 'dialogue'）
        :return: 微调数据
        """
        if tConfig["task_type"] == "question":
            data = self.data_generator.generate_question(tConfig)
        elif tConfig["task_type"] == "answer":
            data = self.data_generator.generate_answer(tConfig)
        elif tConfig["task_type"] == "dialogue":
            data = self.data_generator.generate_dialogue(tConfig)
        else:
            raise ValueError("Unsupported task type")

        return data
