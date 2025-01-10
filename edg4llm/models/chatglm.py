import os
import requests
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Union, cast

from edg4llm.utils.logger import custom_logger
from edg4llm.models.baseModel import EDGBaseModel
from edg4llm.exceptions import HttpClientError, InvalidPromptError

logger = custom_logger('chatglm')

class EDGChatGLM(EDGBaseModel):
    """
    EDGChatGLM interface for interacting with the ChatGLM model to generate text based on given prompts.

    This class provides an interface to interact with the ChatGLM model for generating text 
    based on a system and user prompt. It supports customizable parameters such as temperature, 
    sampling strategies, and model selection. It also handles HTTP requests and error management.

    Parameters
    ----------
    base_url : str, optional
        The base URL for the ChatGLM API. If not provided, defaults to None.
    api_key : str, optional
        The API key for authenticating with the ChatGLM API. If not provided, defaults to None.
    """

    def __init__(self, base_url: str = None, api_key: str = None):
        """
        Initialize the ChatGLM model interface.

        This constructor initializes the `EDGChatGLM` class by calling the base class constructor
        and passing the API key, base URL, and model name ("ChatGLM"). It sets up the necessary 
        configuration for interacting with the ChatGLM API.

        Parameters
        ----------
        base_url : str, optional
            The base URL for the ChatGLM API. Default is None.
        api_key : str, optional
            The API key for authenticating with the ChatGLM API. Default is None.

        Notes
        -----
        The base URL and API key are required for successful communication with the ChatGLM API.
        """
        super().__init__(api_key, base_url, model_name='ChatGLM')

    def execute_request(
            self,
            system_prompt: str = None,
            user_prompt: str = None,
            model: str = "glm-4-flash",
            do_sample: bool = True,
            temperature: float = 0.95,
            top_p: float = 0.7,
            max_tokens: int = 4095
    ) -> str:
        """
        Generate text using the ChatGLM model based on the provided prompts and parameters.

        This method calls the internal request execution function and handles the text 
        generation process using the specified system and user prompts. It allows controlling 
        text generation via parameters such as temperature, sampling strategy, and token limits.

        Parameters
        ----------
        system_prompt : str, optional
            The system-level prompt that sets the context for the conversation. Default is None.
        user_prompt : str, optional
            The user-provided prompt that initiates the conversation. Default is None.
        model : str, optional
            The model to use for generation. Default is "glm-4-flash".
        do_sample : bool, optional
            Whether to use sampling during text generation. Default is True.
        temperature : float, optional
            Sampling temperature to control randomness. Default is 0.95.
        top_p : float, optional
            Nucleus sampling parameter for controlling randomness. Default is 0.7.
        max_tokens : int, optional
            The maximum number of tokens to generate in the output. Default is 4095.

        Returns
        -------
        str
            The generated text content from the model.

        Raises
        ------
        InvalidPromptError
            If both the system and user prompts are None.
        """
        response = self._execute_request(system_prompt, user_prompt, model, do_sample, temperature, top_p, max_tokens)
        return response

    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send an HTTP request to the ChatGLM API.

        This method sends a POST request to the ChatGLM API with the provided request data.
        It returns the response data as a dictionary.

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
        Internal method to send a POST request to the ChatGLM API.

        This method handles the actual HTTP POST request to the ChatGLM API. It includes 
        error handling for HTTP errors, connection issues, timeouts, and JSON decoding.

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
            If an error occurs during the request.
        """
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
            # Handle HTTP error exceptions
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
            # Handle any generic request exceptions
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
            # Catch any unexpected errors
            logger.critical(
                "An unexpected error occurred while sending request to %s: %s", url, e
            )
            raise HttpClientError(
                f"An unexpected error occurred while sending request to {url}: {e}"
            ) from e

    def _execute_request(
            self,
            system_prompt: str = None,
            user_prompt: str = None,
            model: str = "glm-4-flash",
            do_sample: bool = True,
            temperature: float = 0.95,
            top_p: float = 0.7,
            max_tokens: int = 4095
    ) -> str:
        """
        Internal method to prepare the request data and execute the request for text generation.

        This method prepares the necessary data (including headers, JSON body) for the 
        ChatGLM API request and then calls the `send_request` method to send the request 
        and return the response.

        Parameters
        ----------
        system_prompt : str, optional
            The system-level prompt that provides context for the dialogue generation.
            Default is None.
        user_prompt : str, optional
            The user-provided prompt that initiates the generation.
            Default is None.
        model : str, optional
            The model to use for the generation. Default is "glm-4-flash".
        do_sample : bool, optional
            Whether to use sampling during text generation. Default is True.
        temperature : float, optional
            Sampling temperature to control randomness. Default is 0.95.
        top_p : float, optional
            Nucleus sampling parameter for controlling randomness. Default is 0.7.
        max_tokens : int, optional
            The maximum number of tokens to generate. Default is 4095.

        Returns
        -------
        str
            The generated text content from the model.

        Raises
        ------
        InvalidPromptError
            If both the system and user prompts are None.
        """
        if (system_prompt is None and user_prompt is None):
            logger.error("Both prompts cannot be empty")
            raise InvalidPromptError("Both prompts cannot be empty")

        request_data = {
            "url": f"{self.base_url}",
            "headers": {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            "json": {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "do_sample": do_sample,
                "temperature": temperature,
                "top_p": top_p,
                "max_tokens": max_tokens,
            },
        }

        response = self.send_request(request_data)
        return response["choices"][0]["message"]["content"].strip()
