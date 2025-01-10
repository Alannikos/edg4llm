import os
from abc import ABC, abstractmethod
from typing import Dict

from edg4llm.processor.postprocess import PostProcessor
class BaseGenerator(ABC):
    """
    Base class for all data generators, defining a common interface for generating data.

    This class serves as a foundation for different types of data generators, providing common functionality
    such as interaction with a model and post-processing of generated data. Specific generators should extend
    this class and implement their own `generate` method.

    Attributes
    ----------
    model : object
        The model interface used for generating data.
    postprocessor : PostProcessor
        An instance of the PostProcessor class for handling post-processing of generated data.

    Methods
    -------
    generate(prompt: str) -> str
        Abstract method to generate data based on a prompt. Must be implemented by subclasses.

    """
    def __init__(self, model):
        """
        Initialize the generator.

        Parameters
        ----------
        model : object
            The model interface used for generating data.
        """

        self.model = model
        self.postprocessor = PostProcessor()

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Convert original data into Alpaca format.

        This method uses the PostProcessor to process conversation data and structure it
        in a format suitable for Alpaca-based models.

        Parameters
        ----------
        system_prompt : str
            The system-level prompt for context in the Alpaca format.
        single_data : str
            The raw conversation data to be processed.

        Returns
        -------
        dict
            The conversation data converted to Alpaca format.
        """
        pass

    def _convert_original_to_alpaca(self, system_prompt, single_data):
        """
        Convert original data into Alpaca format.

        This method uses the PostProcessor to process conversation data and structure it
        in a format suitable for Alpaca-based models.

        Parameters
        ----------
        system_prompt : str
            The system-level prompt for context in the Alpaca format.
        single_data : str
            The raw conversation data to be processed.

        Returns
        -------
        dict
            The conversation data converted to Alpaca format.
        """

        converted_data = self.postprocessor.dialogue_postprocessing(conversation_data=single_data, system_prompt=system_prompt)

        return converted_data
    
    def _convert_original_to_json(self, single_data):
        """
        Convert original data into JSON format.

        This method uses the PostProcessor to process raw data into a JSON-compatible structure.

        Parameters
        ----------
        single_data : str
            The raw question data to be processed.

        Returns
        -------
        dict
            The data converted into JSON format.
        """

        converted_data = self.postprocessor.question_postprocessing(question_data=single_data)

        return converted_data

    def _convert_original_to_alpaca_answer(self, system_prompt, question, single_data):
        """
        Convert original data into Alpaca answer format.

        This method uses the PostProcessor to process raw data into an answer format suitable for Alpaca-based models.

        Parameters
        ----------
        system_prompt : str
            The system-level prompt for context in the Alpaca format.
        question : str
            The question text for which the answer is generated.
        single_data : str
            The raw answer data to be processed.

        Returns
        -------
        dict
            The data converted into Alpaca format.
        """

        converted_data = self.postprocessor.answer_postprocessing(question=question, answer=single_data, system_prompt=system_prompt)

        return converted_data
    