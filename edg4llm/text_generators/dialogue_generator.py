import os
from typing import Dict, Any

from edg4llm.utils.logger import custom_logger
from edg4llm.text_generators.base_generator import BaseGenerator

logger = custom_logger("DialogueGenerator")

class DialogueGenerator(BaseGenerator):
    """
    Dialogue Generator class for generating dialogues using a specified model.

    This class extends the `BaseGenerator` and utilizes the given model to generate dialogues 
    based on user input and system prompts. It provides flexibility to control generation parameters 
    like sampling strategies, temperature, and output format.

    Parameters
    ----------
    model : object
        The model interface used for generating dialogues. This model must have the 
        `execute_request` method for generating dialogue based on the given parameters.
    """

    def __init__(self, model):
        """
        Initialize the Dialogue Generator.

        This constructor initializes the `DialogueGenerator` by calling the base class constructor
        with the provided model. It sets up the necessary components for generating dialogues.

        Parameters
        ----------
        model : object
            The model interface to be used for generating dialogues. It should provide 
            the `execute_request` method to generate data based on the parameters.

        Notes
        -----
        The `model` should be capable of handling inputs like system prompts, user prompts, 
        and additional parameters for controlling the text generation process.
        """
        super().__init__(model)

    def generate(self, tConfig) -> list:
        """
        Generate dialogues based on the provided configuration.

        This method generates one or more dialogues based on the parameters provided in 
        the `tConfig` dictionary. The method interacts with the model's `execute_request` 
        function to generate dialogue based on the system and user prompts. It also supports 
        various options for controlling randomness, output length, and sampling strategy.

        Parameters
        ----------
        tConfig : dict
            A configuration dictionary containing the following key-value pairs:
            - "system_prompt" : str, optional
                A system-level prompt that guides the dialogue generation. Default is an empty string.
            - "user_prompt" : str, optional
                A user-provided prompt to initiate the dialogue generation. Default is an empty string.
            - "model" : str, optional
                The specific model to use for generation. Default is "glm-4-flash".
            - "do_sample" : bool, optional
                Whether to use sampling strategies during text generation. Default is True.
            - "temperature" : float, optional
                A sampling parameter to control the randomness of output. Must be between 0.0 and 1.0. Default is 0.95.
            - "top_p" : float, optional
                Nucleus sampling parameter controlling the cumulative probability range for token selection. 
                Must be between 0.0 and 1.0. Default is 0.7.
            - "max_tokens" : int, optional
                The maximum number of tokens to generate. Default is 4095.
            - "num_samples" : int, optional
                The number of dialogue samples to generate. Default is 1.
        
        Returns
        -------
        list of dict
            A list of dictionaries containing the generated dialogues. Each dictionary 
            includes the generated dialogue content.

        Notes
        -----
        - The method will attempt to generate dialogues until a valid response is generated. 
          If the generated dialogue is `None`, it will retry.
        - Progress is logged for each sample generated.
        """

        # Extract configuration parameters
        system_prompt = tConfig.get("system_prompt", "")
        user_prompt = tConfig.get("user_prompt", "")
        do_sample = tConfig.get("do_sample", True)
        temperature = tConfig.get("temperature", 0.95)
        top_p = tConfig.get("top_p", 0.7)
        max_tokens = tConfig.get("max_tokens", 4095)
        num_samples = tConfig.get("num_samples", 1)  # Default is to generate 1 sample

        # List to store the generated dialogues
        dialogues = []

        # Generate dialogues for the specified number of samples
        total_samples = num_samples  # Total number of samples to generate
        for _idx in range(1, num_samples + 1):
            while True:  # Keep trying until valid dialogue data is generated
                generated_dialogue = self.model.execute_request(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    do_sample=do_sample,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                )

                # Convert the generated dialogue to the desired format (e.g., Alpaca format)
                converted_generated_dialogue = self._convert_original_to_alpaca(system_prompt, generated_dialogue)

                if converted_generated_dialogue is not None:
                    # If the dialogue is valid, append it to the results and break the loop
                    dialogues.append(converted_generated_dialogue)
                    break
                else:
                    logger.warning("Generated dialogue for sample %d is None. Retrying...", _idx)

            # Log the progress of dialogue generation
            progress = (_idx / total_samples) * 100
            logger.info("Data generation progress: %.2f%% (%d/%d samples completed)", progress, _idx, total_samples)

        return dialogues
