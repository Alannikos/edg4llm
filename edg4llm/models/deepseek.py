import os
import json
import requests
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union, cast

from edg4llm.utils.logger import custom_logger
from edg4llm.models.baseModel import EDGBaseModel
from edg4llm.exceptions import HttpClientError, InvalidPromptError

logger = custom_logger('deepseek')

class EDGDeepSeek(EDGBaseModel):
    def __init__(self, base_url:str = None, api_key: str = None, model_name: str = "deepseek-chat"):
        """
        初始化 DeepSeek 模型接口
        :param base_url: url地址
        :param api_key: DeepSeek 的 API 密钥
        """
        super().__init__(api_key=api_key, base_url=base_url, model_name = model_name)

    def execute_request(
            self
            , system_prompt: str = None
            , user_prompt: str = None
            , do_sample: bool = True
            , temperature: float = 0.95
            , top_p: float = 0.7
            , max_tokens: int = 4095
            ) -> str:
        """
        调用模型生成数据

        :param prompt: 提供给模型的提示文本
        :param model: 模型的名称，默认为 "deepseek-chat"
        :return: 生成的文本
        """

        response = self._execute_request(system_prompt, user_prompt, self.model_name, do_sample, temperature, top_p, max_tokens)
        return response

    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        response = self._send_request(request=request)
        return response

    def _send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:

        url = request.get("url", "https://api.deepseek.com/chat/completions")
        headers = {**request.get("headers", {})}
        data = request.get("data", {})

        if isinstance(data, dict):
            data = json.dumps(data)

        try:
            response = requests.request(
                "POST",
                url=url,
                headers=headers,
                data=data,
                # timeout=30,
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
            , model: str = "deepseek-chat"
            , do_sample: bool = True
            , temperature: float = 0.95
            , top_p: float = 0.7
            , max_tokens: int = 2047
            ) -> str:

        if (system_prompt is None and user_prompt is None):
            logger.error("prompt不能同时为空")
            raise InvalidPromptError("prompt不能同时为空")

        request_data = {
            "url": self.base_url,
            "data": {
                "messages": [
                    {"content": system_prompt, "role": "system"},
                    {"content": user_prompt, "role": "user"}
                ],
                "model": model,
                "frequency_penalty": 0,
                "max_tokens": max_tokens,
                "presence_penalty": 0,
                "response_format": {"type": "text"},
                "stop": None,
                "stream": False,
                "stream_options": None,
                "temperature": temperature,
                "top_p": top_p,
                "tools": None,
                "tool_choice": "none",
                "logprobs": False,
                "top_logprobs": None
            },
            "headers": {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {self.api_key}'
            }
        }

        response = self._send_request(request_data)
        return response["choices"][0]["message"]["content"].strip()
