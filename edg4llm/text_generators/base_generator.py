
"""
    这里应该要能够实现多条数据的生成了
"""

import os
from abc import ABC, abstractmethod

from edg4llm.config import DefaultConfig

class BaseGenerator(ABC):
    """
    所有生成器的基类，定义生成数据的公共接口
    """
    def __init__(self, model_name):
        """
        初始化生成器

        :param model: 用于生成数据的模型接口
        """
        self.model_name = model_name

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        生成数据的接口方法，不同子类应该实现不同的生成逻辑

        :param prompt: 提供给模型的提示文本
        :return: 生成的文本数据
        """
        pass
