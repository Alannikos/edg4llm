import requests
from abc import ABC, abstractmethod
from typing import Any, Dict

from edg4llm.utils.logger import custom_logger

logger = custom_logger('baseModel')

class EDGBaseModel(ABC):
    def __init__(self, api_key: str = None, base_url: str = None, model_name:str = None):
        self.api_key = api_key  # api_key
        self.base_url = base_url  # 模型的url地址
        self.model_name = model_name  # 模型名称，为了区分不同的模型

    @abstractmethod
    def execute_request(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        """
        抽象方法，放到每个具体的模型下面进行实现，然后主要是prompt，这个应该是用户对角色的一种定义
        ，比如是一个会夸赞的好人等等之类的，然后kwargs就是其他参数

        """

        pass

    @abstractmethod
    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        发送http请求的方法，传入的request应该是包含了所有信息，然后这里对异常的判断应该要更加精细一些
        """

        pass
