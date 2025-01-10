import re
import sys
import json

from edg4llm.utils.logger import custom_logger
from edg4llm.utils.data_utils import is_question_template_consistent
from edg4llm.utils.data_utils import is_answer_template_consistent
from edg4llm.utils.data_utils import is_dialogue_template_consistent

from edg4llm.utils.template import Template

logger = custom_logger("preprocess")

class PreProcessor:
    """
    A class for pre-processing user prompts before data generation.

    This class provides methods to validate and repair user prompts in different modes such as question, 
    answer, and dialogue. If a user prompt does not match the expected template, the methods automatically 
    append the corresponding format guidelines to ensure consistency.

    Methods
    -------
    question_preprocess(user_prompt: str) -> str:
        Validates and repairs user prompts in question mode.

    answer_preprocess(user_prompt: str) -> str:
        Validates and repairs user prompts in answer mode.

    dialogue_preprocess(user_prompt: str) -> str:
        Validates and repairs user prompts in Q&A (dialogue) mode.
    """
    def __init__(self):
        pass

    def question_preprocess(self, language: str, user_prompt: str) -> str:
        """
        Validates and processes user prompts in question mode.

        Parameters
        ----------
        language : str
            The language of data in data generation. Must be one of 'zh', 'en'. 

        user_prompt : str
            The user's input prompt to be processed in question mode.

        Returns
        -------
        str
            The validated and, if necessary, repaired user prompt.

        Notes
        -----
        - If the user prompt matches the question template, it is returned unchanged.
        - If the user prompt does not match, format guidelines from `Template.question_template` 
          are appended to the prompt.
        """
        
        if is_question_template_consistent(user_prompt=user_prompt):
            logger.info("User prompt matches the question template. Proceeding with data generation.")
            return user_prompt
        else:
            logger.warning("User prompt does not match the question template. Automatically added format guidelines.")
            if language == "zh":
                repaired_user_prompt = user_prompt + '\n' + Template.question_zh_template
            else:
                repaired_user_prompt = user_prompt + '\n' + Template.question_en_template
            return repaired_user_prompt

    def answer_preprocess(self, language: str, user_prompt: str) -> str:
        """
        Validates and processes user prompts in answer mode.

        Parameters
        ----------
        language : str
            The language of data in data generation. Must be one of 'zh', 'en'. 

        user_prompt : str
            The user's input prompt to be processed in answer mode.

        Returns
        -------
        str
            The validated and, if necessary, repaired user prompt.

        Notes
        -----
        - If the user prompt matches the answer template, it is returned unchanged.
        - If the user prompt does not match, format guidelines from `Template.answer_template` 
          are appended to the prompt.
        """

        if is_answer_template_consistent(user_prompt=user_prompt):
            logger.info("User prompt matches the answer template. Proceeding with data generation.")
            return user_prompt
        else:
            logger.warning("User prompt does not match the answer template. Automatically added format guidelines.")
            if language == "zh":
                repaired_user_prompt = user_prompt + '\n' + Template.answer_zh_template
            else:
                repaired_user_prompt = user_prompt + '\n' + Template.answer_en_template
            return repaired_user_prompt
        
    def dialogue_preprocess(self, language: str, user_prompt: str) -> str:
        """
        Validates and processes user prompts in Q&A (dialogue) mode.

        Parameters
        ----------
        language : str
            The language of data in data generation. Must be one of 'zh', 'en'. 

        user_prompt : str
            The user's input prompt to be processed in Q&A mode.

        Returns
        -------
        str
            The validated and, if necessary, repaired user prompt.

        Notes
        -----
        - If the user prompt matches the dialogue template, it is returned unchanged.
        - If the user prompt does not match, format guidelines from `Template.dialogue_template` 
          are appended to the prompt.
        """

        if is_dialogue_template_consistent(user_prompt=user_prompt):
            logger.info("User prompt matches the dialogue template. Proceeding with data generation.")
            return user_prompt
        else:
            logger.warning("User prompt does not match the dialogue template. Automatically added format guidelines.")
            if language == "zh":
                repaired_user_prompt = user_prompt + '\n' + Template.dialogue_zh_template
            else:
                repaired_user_prompt = user_prompt + '\n' + Template.dialogue_en_template
            return repaired_user_prompt
