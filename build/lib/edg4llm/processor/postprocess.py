import json
from typing import Dict, List, Any

from edg4llm.utils.logger import custom_logger

logger = custom_logger("PostProcessor")

class PostProcessor:
    """
    A class for post-processing conversation and question data.

    This class provides methods to clean and structure raw data obtained from API responses or external sources.
    It handles the removal of unnecessary markdown formatting, parses the data into valid JSON format, and
    structures it for further use in applications such as chatbots or AI assistants. It can also incorporate
    an optional system prompt into the processed data for context.

    Methods
    -------
    dialogue_postprocessing(conversation_data: Dict[str, str], system_prompt: str = None):
        Processes raw conversation data by cleaning, parsing, and adding an optional system prompt.

    question_postprocessing(question_data: str = None):
        Processes raw question data by cleaning and structuring it into a list of questions.

    answer_postprocessing(question: str, answer: str, system_prompt: str = None):
        Processes raw answer data by cleaning, parsing, and structuring it along with the question
        and an optional system prompt.
    """
    
    def __init__(self):
        pass

    def dialogue_postprocessing(self, conversation_data: Dict[str, str], system_prompt: str = None):
        """
        Post-process conversation data.

        This function processes raw conversation data by removing unnecessary formatting and parsing it 
        into a valid JSON format. If a system-level prompt (system_prompt) is provided, it will be added 
        as an "instruction" field to the first conversation entry. The processed data is returned as a 
        dictionary with a "conversation" key.

        Parameters
        ----------
        conversation_data : str
            The raw conversation data in string format, typically from an API response or an external source.
            It may contain markdown-style formatting such as "```json" or "```" that needs to be removed.

        system_prompt : str, optional
            An optional system-level prompt that will be added to the "instruction" field of the first 
            conversation entry. If not provided, an empty string will be used. Default is None.

        Returns
        -------
        dict or None
            Returns a dictionary containing the processed conversation data structured under the "conversation" key.
            Each item in the list corresponds to a conversation entry. If an error occurs during JSON parsing, 
            the function logs the error and returns None.

        Examples
        --------
        >>> conversation_data = '''
            [
                {"input": "AAA", "output": "BBBB"},
                {"input": "CCC", "output": "DDDD"}
            ]
        '''
        >>> system_prompt = "You are a helpful assistant."
        >>> processed_data = postprocessing(conversation_data, system_prompt)

        >>> # Output:
        >>> {
            "conversation": [
                {"input": "AAA", "output": "BBBB", "instruction": "You are a helpful assistant."},
                {"input": "CCC", "output": "DDDD"}
            ]
        }

        Notes
        -----
        - The function removes any markdown formatting (like "```json" or "```") before parsing the data.
        - If JSON parsing fails, an error is logged, and the function returns None.
        """
        try:
            # Clean and parse the JSON conversation data
            conversation_data = json.loads(conversation_data.replace("```json", "").replace("```", ""))
        except Exception as exception:
            logger.error("Error parsing JSON: %s", str(exception))
            return None

        # Initialize the result dictionary with a "conversation" key
        result = {"conversation": []}

        # Add the system prompt as an instruction to the first conversation entry if provided
        for idx, data in enumerate(conversation_data):
            if idx == 0:
                data["instruction"] = system_prompt if system_prompt is not None else ""
            result["conversation"].append(data)

        return result


    def question_postprocessing(self, question_data: str = None):
        """
        Post-process the question data.

        This function processes raw question data by removing unnecessary formatting and ensuring 
        it is in a valid JSON format. It converts each question into a structured dictionary with 
        the key "question" holding the processed content.

        Parameters
        ----------
        question_data : str
            The raw question data in string format, typically from an API response or external source.
            The string may contain markdown-style formatting such as "```json" or "```" that should be removed.

        Returns
        -------
        dict or None
            Returns a dictionary with the format {"question": <processed_question_content>}. 
            If an error occurs during JSON parsing, it returns None.

        Examples
        --------
        >>> question_data = "What is your name?"
        >>> processed_data = question_postprocessing(question_data)
        >>> print(processed_data)
        Output: {'question': 'What is your name?'}

        Notes
        -----
        - This function removes any markdown formatting (e.g., "```json" or "```") from the input string.
        - If an exception occurs during JSON parsing, an error message is logged, and the function returns None.
        """

        try:
            # Clean up and parse the JSON question data
            question_data = json.loads(question_data.replace("```json", "").replace("```", ""))
        except Exception as exception:
            logger.error("Error parsing JSON: %s", str(exception))
            return None

        # Initialize the result with a "question" key
        result = []

        # Extract the question and assign it to the result
        for _, data in enumerate(question_data):
            result.append(data)

        return result

    def answer_postprocessing(self, question: str, answer: str, system_prompt: str = None):
        """
        Post-process conversation data.

        This function processes raw conversation data by parsing it into a valid JSON format and structuring 
        it into a predefined format. It also adds an optional system prompt to each conversation entry 
        under the "instruction" key. The processed data is returned as a dictionary wrapped in a list.

        Parameters
        ----------
        question : str
            The input question or query from the user.

        answer : str
            The raw answer data in string format, typically containing JSON content.
            This string may contain markdown formatting (e.g., "```json" or "```") that needs to be removed.

        system_prompt : str, optional
            An optional system-level prompt to provide context or instructions. This will be added to 
            each conversation entry under the "instruction" key. Default is None.

        Returns
        -------
        list or None
            Returns a list containing a dictionary with the processed conversation data.
            The dictionary has a "conversation" key, which is a list of conversation entries.
            Each entry contains "input", "output", and "instruction" keys.
            If an error occurs during JSON parsing, the function logs the error and returns None.

        Examples
        --------
            >>> # Input:
            >>> question = "What is AI?"
            >>> answer = '''
                [
                    {
                        "input": question, 
                        "output": "BBB"
                    }
                ]
            '''
            >>> system_prompt = "You are a helpful assistant."

            >>> # Function Call:
            >>> processed_data = answer_postprocessing(question, answer, system_prompt)

            >>> # Output:
            >>> [
                {
                    "conversation": [
                        {
                            "input": "What is AI?", 
                            "output": "BBB", 
                            "instruction": "You are a helpful assistant."
                        }
                    ]
                }
            ]

        Notes
        -----
        - The function removes any markdown formatting (like "```json" or "```") before parsing the data.
        - If JSON parsing fails, the function logs an error and returns None.
        - The output is wrapped in a list to allow for future extensibility.
        """

        try:
            # Clean up and parse the JSON conversation data
            conversation_data = json.loads(answer.replace("```json","").replace("```",""))
        except Exception as exception:
            logger.error("Error parsing JSON: %s", str(exception))
            return None

        # Initialize the result with a conversation key
        result = {"conversation": []}
        conversation = {"instruction" : system_prompt, "input" : question}
        # Add the system prompt to the first conversation entry if provided
        for idx, data in enumerate(conversation_data):
            conversation['output'] = data["answer"]
            result["conversation"].append(conversation)
        return result
