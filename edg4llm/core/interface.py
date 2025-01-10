"""
EDG4LLM: A Comprehensive Interface for Text Generation with Configurable LLMs

Overview
--------
The EDG4LLM class serves as a high-level interface for generating text using a language model pipeline. 
It supports configuration for task types, prompts, sampling strategies, and output formats, making it versatile 
and adaptable to various use cases.

Key Features
------------
- Task Flexibility: Supports task types such as 'dialogue', 'question', and 'answer'.
- Custom Prompts: Allows system-level and user-level prompts to guide the generation process.
- Sampling Controls: Provides options to customize randomness and diversity of outputs using 
  parameters like `do_sample`, `temperature`, and `top_p`.
- Output Formats: Compatible with customizable output formats, such as "alpaca".
"""



import os
from typing import Any, Tuple, Dict

from edg4llm.utils.logger import custom_logger
from edg4llm.core.pipeline import DataPipeline

logger = custom_logger("interface")


class EDG4LLM:
    """
    EDG4LLM: A Class for Configurable Text Generation with LLMs

    This class provides an interface for generating text using a configurable language model pipeline. 
    It allows users to specify a variety of parameters, including model type, prompts, sampling strategies, 
    and output formats.

    Attributes
    ----------
    pipeline : DataPipeline
        An instance of the `DataPipeline` class, used to handle the data processing 
        and interaction with the language model.

    Methods
    -------
    __init__(model_provider: str = "chatglm", model_name: str = "chatglm-4-flash", base_url: str = None, api_key: str = None):
        Initializes the EDG4LLM instance with the model type, base URL, and API key.

    generate(task_type: str = 'dialogue', system_prompt: str = None, user_prompt: str = None, 
            do_sample: bool = True, temperature: float = 0.95, top_p: float = 0.7, 
            max_tokens: int = 4095, num_samples: int = 10, output_format: str = "alpaca") -> list[dict]:
        Generates text data based on the provided configuration.

    Notes
    -----
    - This class leverages the `DataPipeline` for all interactions with the language model.
    - The `generate` method is user-facing.
    - Supports customization for tasks like 'dialogue', 'question', and 'answer'.
    - Ensures compatibility with different output formats (e.g., "alpaca").

    Examples
    --------
    >>> # Create an instance of EDG4LLM
    >>> generator = EDG4LLM(model_provider="chatglm", model_name="chatglm-4-flash", base_url="https://api.example.com", api_key="your_api_key")

    >>> # Generate a dialogue response
    >>> response = generator.generate(
        task_type="answer",
        system_prompt="You are a helpful assistant.",
        user_prompt="What is the weather today?",
        max_tokens=100
    )

    >>> print(response)
    Output: [{'output': 'The weather today is sunny with a high of 25°C.'}]
    """
    def __init__(self,
                 model_provider: str = "chatglm",
                 model_name: str = "chatglm-4-flash",
                 base_url: str = None,
                 api_key: str = None):
        """
        Initialize the EDG4LLM instance with the necessary parameters.

        Parameters
        ----------
        model_provider: str, optional
            The type of language model to use, by default "chatglm".
        model_name : str, optional
            The specific model to use within the model type, by default "chatglm-4-flash".
        base_url : str, optional
            The base URL of the LLM API, by default None.
        api_key : str, optional
            The API key for authenticating requests, by default None.
        """

        self._pConfig = {
            "model_provider": model_provider
            ,"model_name" : model_name
            , "base_url": base_url
            , "api_key" : api_key
        }

        self.pipeline = DataPipeline(self._pConfig)
        logger.info("DataPipeline initialized successfully with the provided configuration.")

    def generate(self
                , task_type: str = 'dialogue'
                , system_prompt: str = None
                , user_prompt: str = None
                , do_sample: bool = True
                , temperature: float = 0.95
                , top_p: float = 0.7
                , max_tokens: int = 4095
                , num_samples: int = 10
                , output_format: str = "alpaca"
                ):
        """
        Generate text data based on the specified configuration.

        Parameters
        ----------
        task_type : str, optional
            The type of task for data generation. Must be one of 'question', 'answer', or 'dialogue'. 
            Default is 'dialogue'.

        system_prompt : str, optional
            A system-level prompt to guide the text generation. 
            Default is None.

        user_prompt : str, optional
            A user-provided prompt to initiate the text generation. 
            Default is None.

        do_sample : bool, optional
            Whether to use sampling during text generation.
            - If True, enables sampling strategies like temperature and top_p.
            - If False, uses deterministic decoding (e.g., greedy decoding), and
            `temperature` and `top_p` are ignored.
            Default is True.

        temperature : float, optional
            Sampling temperature to control randomness.
            - Must be a positive number in the range [0.0, 1.0].
            - Higher values produce more diverse outputs, while lower values make 
            the output more focused and deterministic.
            Default is 0.95.

        top_p : float, optional
            Nucleus sampling parameter for controlling randomness.
            - Limits token selection to the top cumulative probability range 
            defined by p.
            - Must be in the range [0.0, 1.0].
            Default is 0.7.

        max_tokens : int, optional
            The maximum number of tokens to generate in the output.
            - Default: 4095.
            - Maximum allowed value: 4095 (values exceeding this will be capped).

        num_samples : int, optional
            The number of output samples to generate. 
            Default is 10.

        output_format : str, optional
            The format of the output. 
            Default is "alpaca".

        Returns
        -------
        list of dict
            A list of dictionaries containing the generated outputs.

        Examples
        --------
        >>> # Create an instance of EDG4LLM
        >>> generator = EDG4LLM(model_provider="chatglm", model_name="chatglm-4-flash", base_url="https://api.example.com", api_key="your_api_key")

        >>> # Generate a dialogue response
        >>> response = generator.generate(
            task_type="answer",
            system_prompt="You are a helpful assistant.",
            user_prompt="What is the weather today?",
            max_tokens=100
        )

        >>> print(response)
        Output: [{'output': 'The weather today is sunny with a high of 25°C.'}]

        Notes
        -----
        The method will use a pipeline's `generate_data` function to create outputs
        based on the provided configuration.
        """

        data = self._generate(task_type, system_prompt, user_prompt, do_sample, temperature, top_p, max_tokens, num_samples, output_format)
        logger.info("Data generation completed successfully for task_type: %s", task_type)
        
        return data

    def _generate(self,
                task_type: str = 'dialogue',
                system_prompt: str = None,
                user_prompt: str = None,
                do_sample: bool = True,
                temperature: float = 0.95,
                top_p: float = 0.7,
                max_tokens: int = 4095,
                num_samples: int = 10,
                output_format: str = "alpaca"):
        """
        Generate text data based on the specified configuration.

        Parameters
        ----------
        task_type : str, optional
            The type of task for data generation. Must be one of 'question', 'answer', or 'dialogue'. 
            Default is 'dialogue'.

        system_prompt : str, optional
            A system-level prompt to guide the text generation. 
            Default is None.

        user_prompt : str, optional
            A user-provided prompt to initiate the text generation. 
            Default is None.

        do_sample : bool, optional
            Whether to use sampling during text generation.
            - If True, enables sampling strategies like temperature and top_p.
            - If False, uses deterministic decoding (e.g., greedy decoding), and
            `temperature` and `top_p` are ignored.
            Default is True.

        temperature : float, optional
            Sampling temperature to control randomness.
            - Must be a positive number in the range [0.0, 1.0].
            - Higher values produce more diverse outputs, while lower values make 
            the output more focused and deterministic.
            Default is 0.95.

        top_p : float, optional
            Nucleus sampling parameter for controlling randomness.
            - Limits token selection to the top cumulative probability range 
            defined by p.
            - Must be in the range [0.0, 1.0].
            Default is 0.7.

        max_tokens : int, optional
            The maximum number of tokens to generate in the output.
            - Default: 4095.
            - Maximum allowed value: 4095 (values exceeding this will be capped).

        num_samples : int, optional
            The number of output samples to generate. 
            Default is 10.

        output_format : str, optional
            The format of the output. 
            Default is "alpaca".

        Returns
        -------
        list of dict
            A list of dictionaries containing the generated outputs.

        Examples
        --------
        >>> # Create an instance of EDG4LLM
        >>> generator = EDG4LLM(model_provider="chatglm", model_name="chatglm-4-flash", base_url="https://api.example.com", api_key="your_api_key")

        >>> # Generate a dialogue response
        >>> response = generator.generate(
            task_type="answer",
            system_prompt="You are a helpful assistant.",
            user_prompt="What is the weather today?",
            max_tokens=100
        )

        >>> print(response)
        Output: [{'output': 'The weather today is sunny with a high of 25°C.'}]

        Notes
        -----
        The method will use a pipeline's `generate_data` function to create outputs
        based on the provided configuration.
        """

        self._tConfig = {
            "task_type": task_type,         # The type of task for data generation
            "system_prompt": system_prompt, # The system-level prompt
            "user_prompt": user_prompt,     # The user-provided prompt
            "do_sample": do_sample,         # Whether to use sampling
            "temperature": temperature,     # Sampling temperature
            "top_p": top_p,                 # Nucleus sampling parameter
            "max_tokens": max_tokens,       # Maximum tokens in the output
            "num_samples": num_samples,     # Number of output samples
            "output_format": output_format  # Desired output format
        }
        
        # Call the pipeline's generate_data method using the configuration dictionary
        data = self.pipeline.generate_data(self._tConfig)

        return data
