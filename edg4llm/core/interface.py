import os
from typing import Any, Tuple, Dict


from edg4llm.core.pipeline import DataPipeline
from edg4llm.config import Config

class Edg4LLM:
    def __init__(self, model_type:str = "chatglm", api_key:str = None, config=None):
        """
        初始化统一接口。
        :param model_type: 模型类型，例如 'openai', 'chatglm'
        :param config: 自定义配置对象（可选）
        """
        self.config = config or Config()
        self.config.update({"model_type": model_type})
        self.pipeline = DataPipeline(self.config)

    def init_model(self, model_type, api_key):
        pass


    def generate(self, task_type, topic=None, count=10, output_format="json"):
        """
        生成数据的统一方法。
        :param task_type: 任务类型，例如 'question', 'answer', 'dialogue'
        :param topic: 生成数据的主题（可选）
        :param count: 生成数据的数量
        :param output_format: 输出数据的格式，例如 'json', 'list'
        :return: 生成的数据
        """

        data = self.pipeline.generate(task_type, topic, count)

        if output_format == "json":
            import json
            return json.dumps(data, ensure_ascii=False, indent=4)
        elif output_format == "list":
            return data
        else:
            raise ValueError(f"Unsupported output_format: {output_format}")

    def _generate(self):
        pass
    