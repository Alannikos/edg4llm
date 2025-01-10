import os
import requests
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union, cast

from edg4llm.utils.logger import custom_logger
from edg4llm.models.baseModel import EDGBaseModel
from edg4llm.exceptions import HttpClientError, InvalidPromptError

logger = custom_logger('chatglm')

class EDGChatGPT(EDGBaseModel):
    def __init__(self, base_url:str = None, api_key: str = None):
        """
        初始化 ChatGLM 模型接口
        :param base_url: url地址
        :param api_key: ChatGLM 的 API 密钥
        """
        super().__init__(api_key, base_url, model_name='ChatGLM')

    def execute_request(
            self
            , system_prompt: str = None
            , user_prompt: str = None
            , model: str = "glm-4-flash"
            , do_sample: bool = True
            , temperature: float = 0.95
            , top_p: float = 0.7
            , max_tokens: int = 4095
            ) -> str:
        """
        调用模型生成数据

        :param prompt: 提供给模型的提示文本
        :param model: 模型的名称，默认为 "glm-4-flash"
        :return: 生成的文本
        """

        response = self._execute_request(system_prompt, user_prompt, model, do_sample, temperature, top_p, max_tokens)
        return response

    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        response = self._send_request(request=request)
        return response

    def _send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:

        url = request.get("url", "https://open.bigmodel.cn/api/paas/v4/chat/completions")
        headers = {**request.get("headers", {})}
        json = request.get("json", {})
        try:
            response = requests.post(
                url=url,
                headers=headers,
                json=json,
                timeout=30,
            )
    
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            # 捕捉http请求的异常
            status_code = e.response.status_code
            logger.error(
                "HTTP error occurred. Status Code: %s, URL: %s, Message: %s",
                status_code,
                url,
                e,
            )
            raise HttpClientError(
                f"HTTP error occurred. Status Code: {status_code}, Message: {e}",
                status_code=status_code,
            ) from e

        except requests.exceptions.ConnectionError as e:
            # Handle connection errors
            logger.error("Connection error occurred while connecting to %s: %s", url, e)
            raise HttpClientError(
                f"Connection error occurred while connecting to {url}: {e}"
            ) from e

        except requests.exceptions.Timeout as e:
            # Handle timeout errors
            logger.error("Timeout occurred while sending request to %s: %s", url, e)
            raise HttpClientError(
                f"Request timed out while connecting to {url}: {e}"
            ) from e

        except requests.exceptions.RequestException as e:
            # Handle generic request exceptions
            logger.error(
                "Request exception occurred while sending request to %s: %s", url, e
            )
            raise HttpClientError(
                f"An unexpected error occurred while making the request to {url}: {e}"
            ) from e

        except ValueError as e:
            # Handle JSON decoding errors
            logger.error("JSON decoding error occurred: %s", e)
            raise HttpClientError(f"JSON decoding error occurred: {e}") from e

        except Exception as e:
            # Catch all other exceptions
            logger.critical(
                "An unexpected error occurred while sending request to %s: %s", url, e
            )
            raise HttpClientError(
                f"An unexpected error occurred while sending request to {url}: {e}"
            ) from e

    def _execute_request(
            self
            , system_prompt: str = None
            , user_prompt: str = None
            , model: str = "glm-4-flash"
            , do_sample: bool = True
            , temperature: float = 0.95
            , top_p: float = 0.7
            , max_tokens: int = 4095
            ) -> str:
        
        if (system_prompt is None and user_prompt is None):
            logger.error("prompt不能同时为空")
            raise InvalidPromptError("prompt不能同时为空")

        request_data = {
            "url": f"{self.base_url}",
            "headers": {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            "json": {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                "do_sample": do_sample,
                "temperature": temperature,
                "top_p": top_p,
                "max_tokens": max_tokens
            },
        }

        response = self.send_request(request_data)
        return response["choices"][0]["message"]["content"].strip()
