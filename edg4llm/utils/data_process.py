import json

from edg4llm.utils.logger import custom_logger

logger = custom_logger("process")

class DataProcessor:
    def __init__(self):
        pass

    def preprocess(self, data: str) -> dict:
        """
        TODO
        """
        
        pass

    def postprocessing(self, conversation_data, system_prompt: str = None):
        """
        Post-process the conversation data.

        This function processes the raw conversation data by removing unnecessary formatting 
        and ensuring it is in a valid JSON format. It also adds an optional system prompt to 
        the first conversation entry if provided. The processed data is returned in a structured 
        format with a 'conversation' key containing the conversation entries.

        Parameters
        ----------
        conversation_data : str
            The raw conversation data in string format, typically from an API response or external source.
            The string may contain markdown-style formatting such as "```json" or "```" that should be removed.

        system_prompt : str, optional
            An optional system-level prompt that can be added to the first conversation entry. 
            If not provided, an empty string will be used for the first entry. Default is None.

        Returns
        -------
        dict or None
            Returns a dictionary containing the post-processed conversation data, structured with a 
            "conversation" key. Each item in the list corresponds to a conversation entry.
            If an error occurs during JSON parsing, returns None.

        Examples
        --------
        >>> conversation_data = '{"role": "user", "content": "Hello!"}, {"role": "system", "content": "Hi, how can I help?"}'
        >>> processed_data = postprocessing(conversation_data, system_prompt="You are a helpful assistant.")
        >>> print(processed_data)
        Output: {'conversation': [{'role': 'user', 'content': 'Hello!', 'instruction': 'You are a helpful assistant.'}, {'role': 'system', 'content': 'Hi, how can I help?'}]}

        Notes
        -----
        - The function removes any markdown formatting (like "```json" or "```") before processing the data.
        - If an exception occurs during JSON parsing, an error message is logged and the function returns None.
        """
        try:
            # Clean up and parse the JSON conversation data
            conversation_data = json.loads(conversation_data.replace("```json","").replace("```",""))
        except Exception as exception:
            logger.error("Error parsing JSON: %s", str(exception))
            return None

        # Initialize the result with a conversation key
        result = {"conversation": []}

        # Add the system prompt to the first conversation entry if provided
        for idx, data in enumerate(conversation_data):
            if idx == 0:
                data['instruction'] = system_prompt if system_prompt is not None else ""
            result["conversation"].append(data)

        return result


def save_data_to_json(data: list[dict], output_path: str):
    """
    Save a list of dictionaries to a JSON file.

    This function takes a list of dictionaries and writes it to a specified JSON file. 
    The JSON file is written in a human-readable format with an indentation of 4 spaces 
    and non-ASCII characters preserved.

    Parameters
    ----------
    data : list of dict
        A list of dictionaries to be saved to a JSON file. Each dictionary should contain 
        the data to be written.
    
    output_path : str
        The path (including the filename) where the JSON data will be saved. 
        The file will be written in UTF-8 encoding.

    Returns
    -------
    None
        This function does not return any value. It saves the data to the specified file.
    
    Examples
    --------
    >>> data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
    >>> save_data_to_json(data, "output.json")

    Notes
    -----
    - The function uses `json.dump` to write the data to the file.
    - Non-ASCII characters are preserved with the `ensure_ascii=False` argument.
    - The file will be saved with an indentation of 4 spaces to make it human-readable.
    """

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
