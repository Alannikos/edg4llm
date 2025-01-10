import os
import json
import requests
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union, cast

from edg4llm.utils.logger import custom_logger
from edg4llm.models.baseModel import EDGBaseModel
from edg4llm.utils.exceptions import HttpClientError, InvalidPromptError

logger = custom_logger('deepseek')

class EDGDeepSeek(EDGBaseModel):
    """
    A class to interface with the DeepSeek model for text generation.

    This class extends the `EDGBaseModel` abstract base class to implement a specific interface 
    for interacting with the DeepSeek API. It allows generating text based on system-level and 
    user-level prompts, with customizable parameters such as temperature, sampling strategies, 
    and token limits. The class includes methods to handle HTTP requests and manage errors 
    specific to the DeepSeek API.

    Attributes
    ----------
    base_url : str
        The base URL for the DeepSeek API endpoint.
    api_key : str
        The API key for authenticating with the DeepSeek API.
    model_name : str
        The specific model to use, defaulting to "deepseek-chat".

    Methods
    -------
    execute_request(system_prompt: str, user_prompt: str, do_sample: bool, temperature: float, top_p: float, max_tokens: int) -> str:
        Generates text using the DeepSeek model based on the provided prompts and parameters.

    send_request(request: Dict[str, Any]) -> Dict[str, Any]:
        Sends an HTTP POST request to the DeepSeek API and returns the response as a dictionary.
        
    Notes
    -----
    - The `base_url` and `api_key` are required for proper communication with the DeepSeek API.
    - Provides detailed error handling for HTTP, connection, timeout, and JSON decoding issues.
    - Supports customizable text generation parameters for flexibility in model behavior.
    """

    def __init__(self, base_url:str = None, api_key: str = None, model_name: str = "deepseek-chat"):
        """
        Initialize the DeepSeek model interface.

        Parameters
        ----------
        base_url : str, optional
            The base URL for the DeepSeek API. Default is None.
        api_key : str, optional
            The API key for authenticating with the DeepSeek API. Default is None.
        model_name : str, optional
            The specific model to use, defaulting to "deepseek-chat".
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
        Generate text using the DeepSeek model based on the provided prompts and parameters.

        Parameters
        ----------
        system_prompt : str, optional
            The system-level prompt providing context for the text generation. Default is None.
        user_prompt : str, optional
            The user-provided prompt initiating the text generation. Default is None.
        do_sample : bool, optional
            Whether to use sampling during text generation. Default is True.
        temperature : float, optional
            Sampling temperature to control randomness. Default is 0.95.
        top_p : float, optional
            Nucleus sampling parameter to control randomness. Default is 0.7.
        max_tokens : int, optional
            The maximum number of tokens to generate. Default is 4095.

        Returns
        -------
        str
            The generated text content from the model.

        Raises
        ------
        InvalidPromptError
            If both system and user prompts are None.
        """

        response = self._execute_request(system_prompt, user_prompt, self.model_name, do_sample, temperature, top_p, max_tokens)
        return response

    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send an HTTP request to the DeepSeek API.

        Parameters
        ----------
        request : dict
            A dictionary containing the request data, including the URL, headers, and JSON body.

        Returns
        -------
        dict
            The response from the API in the form of a dictionary.

        Raises
        ------
        HttpClientError
            If any error occurs during the HTTP request process.
        """

        response = self._send_request(request=request)
        return response

    def _send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Internal method to send an HTTP POST request to the DeepSeek API.

        This method handles the actual HTTP POST request and manages error handling 
        for issues like connection failures, timeouts, and JSON decoding errors.

        Parameters
        ----------
        request : dict
            A dictionary containing the request data, including the URL, headers, and JSON body.

        Returns
        -------
        dict
            The JSON response from the API.

        Raises
        ------
        HttpClientError
            If an error occurs during the HTTP request.
        """

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
            return response.json()["choices"][0]["message"]["content"].strip()

        except requests.exceptions.HTTPError as e:
            # Handle HTTP error exceptions
            status_code = e.response.status_code
            logger.error(
                "HTTP error occurred. Status Code: %s, URL: %s, Message: %s",
                status_code,
                url,
                e,
            )

            return {"error": "HTTP error", "status_code": status_code, "message": str(e)}


        except requests.exceptions.ConnectionError as e:
            # Handle connection errors
            logger.error("Connection error occurred while connecting to %s: %s", url, e)
            
            return {"error": "Connection error", "message": str(e)}

        except requests.exceptions.Timeout as e:
            # Handle timeout errors
            logger.error("Timeout occurred while sending request to %s: %s", url, e)

            return {"error": "Timeout", "message": str(e)}


        except requests.exceptions.RequestException as e:
            # Handle any generic request exceptions
            logger.error(
                "Request exception occurred while sending request to %s: %s", url, e
            )

            return {"error": "Request exception", "message": str(e)}


        except ValueError as e:
            # Handle JSON decoding errors
            logger.error("JSON decoding error occurred: %s", e)

            return {"error": "JSON decoding error", "message": str(e)}

        except Exception as e:
            # Catch any unexpected errors
            logger.critical(
                "An unexpected error occurred while sending request to %s: %s", url, e
            )

            return {"error": "Unexpected error", "message": str(e)}

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

        """
        Internal method to prepare and execute the API request for text generation.

        Parameters
        ----------
        system_prompt : str, optional
            The system-level prompt providing context for the text generation. Default is None.
        user_prompt : str, optional
            The user-provided prompt initiating the text generation. Default is None.
        model : str, optional
            The specific model to use for text generation. Default is "deepseek-chat".
        do_sample : bool, optional
            Whether to use sampling during text generation. Default is True.
        temperature : float, optional
            Sampling temperature to control randomness. Default is 0.95.
        top_p : float, optional
            Nucleus sampling parameter to control randomness. Default is 0.7.
        max_tokens : int, optional
            The maximum number of tokens to generate. Default is 2047.

        Returns
        -------
        str
            The generated text content from the model.

        Raises
        ------
        InvalidPromptError
            If both system and user prompts are None.
        """

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
        
        return response
