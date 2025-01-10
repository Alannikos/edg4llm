import os
from typing import Any, Tuple, Dict

from edg4llm.utils.logger import custom_logger
from edg4llm.core.dataGenerators import DataGenerator

logger = custom_logger("DataPipeline")

class DataPipeline:
    """
    The DataPipeline class manages the entire process of generating data, designed to 
    automatically create fine-tuning data for different task types such as question 
    generation, answer generation, and dialogue generation.

    This class uses a DataGenerator object to handle the core logic of data generation 
    and dynamically executes the corresponding task based on the provided configuration 
    parameters. It provides a unified interface for users to easily invoke specific 
    data generation methods with minimal configuration.

    Attributes:
    ----------
    data_generator (DataGenerator): An object that handles the specific data generation tasks.
    
    Methods:
    ----------
    __init__(pConfig): Initializes the DataPipeline class and creates a DataGenerator 
                        object based on the configuration.
    generate_data(tConfig): Generates fine-tuning data based on the task configuration. 
                            Supported task types include question generation, answer generation, 
                            and dialogue generation.
    """

    def __init__(self, pConfig):
        """
        Initializes the data generation process.

        Parameters
        ----------
        pConfig : dict
            Configuration for initializing the DataGenerator. Expected to contain:
            - model_provider: str
                The type of language model to use, by default "chatglm".
            - model_name: str
                The specific model to use within the model type, by default "chatglm-4-flash".
            - base_url : str
                The base URL of the LLM API.
            - api_key : str
                The API key for authentication.
        """

        self.data_generator = DataGenerator(pConfig)

    def generate_data(self, tConfig) -> dict:
        """
        Generates data based on the provided configuration.

        Parameters
        ----------
        tConfig : dict
            Task configuration containing the following keys:
            - task_type : str
                Specifies the type of task ('question', 'answer', or 'dialogue').
            - Other parameters required for data generation, specific to the task type.

        Returns
        -------
        dict
            A dictionary containing the generated fine-tuning data.

        Raises
        ------
        ValueError
            If the provided task type is unsupported.
        """
        if tConfig["task_type"] == "question":
            logger.info("Generated data for task_type: 'question'")
            data = self.data_generator.generate_question(tConfig)
        elif tConfig["task_type"] == "answer":
            logger.info("Generated data for task_type: 'answer'")
            data = self.data_generator.generate_answer(tConfig)
        elif tConfig["task_type"] == "dialogue":
            logger.info("Generated data for task_type: 'dialogue'")
            data = self.data_generator.generate_dialogue(tConfig)
        else:
            logger.error("Unsupported task type: %s", tConfig["task_type"])
            raise ValueError("Unsupported task type")

        return data
