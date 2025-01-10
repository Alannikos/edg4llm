import json
import re

def is_question_template_consistent(user_prompt: str) -> bool:
    """
    Check if the user prompt contains a consistent question JSON template.

    Parameters
    ----------
    user_prompt : str
        The user-provided prompt to be validated.

    Returns
    -------
    bool
        True if the user prompt contains a valid and consistent question JSON template,
        False otherwise.

    Notes
    -----
    - The function uses a regular expression to extract the JSON template and compares it 
      with the target template.
    - The target template is:
      [
          {
              "question": "AAA"
          }
      ]
    - Returns False if the JSON extraction or comparison fails.
    """
    target_template = [
        {
            "question": "AAA"
        }
    ]
    
    # Regular expression to extract JSON template
    pattern = r"\[\s*{\s*\"question\"\s*:\s*\"AAA\"\s*}\s*\]"
    match = re.search(pattern, user_prompt)
    
    if match:
        try:
            extracted_template = json.loads(match.group(0))
        except json.JSONDecodeError:
            return False
        return extracted_template == target_template
    return False

def is_answer_template_consistent(user_prompt: str) -> bool:
    """
    Check if the user prompt contains a consistent answer JSON template.

    Parameters
    ----------
    user_prompt : str
        The user-provided prompt to be validated.

    Returns
    -------
    bool
        True if the user prompt contains a valid and consistent answer JSON template,
        False otherwise.

    Notes
    -----
    - The function uses a regular expression to extract the JSON template and compares it 
      with the target template.
    - The target template is:
      [
          {
              "answer": "AAA"
          }
      ]
    - Returns False if the JSON extraction or comparison fails.
    """
    target_template = [
        {
            "answer": "AAA"
        }
    ]
    
    # Regular expression to extract JSON template
    pattern = r"\[\s*{\s*\"answer\"\s*:\s*\"AAA\"\s*}\s*\]"
    match = re.search(pattern, user_prompt)
    
    if match:
        try:
            extracted_template = json.loads(match.group(0))
        except json.JSONDecodeError:
            return False
        return extracted_template == target_template
    return False

def is_dialogue_template_consistent(user_prompt: str) -> bool:
    """
    Check if the user prompt contains a consistent dialogue JSON template.

    Parameters
    ----------
    user_prompt : str
        The user-provided prompt to be validated.

    Returns
    -------
    bool
        True if the user prompt contains a valid and consistent dialogue JSON template,
        False otherwise.

    Notes
    -----
    - The function uses a regular expression to check for the dialogue JSON structure.
    - The expected template format is:
      [
          {
              "input": "AAA",
              "output": "BBB"
          }
      ]
    """

    pattern = r"\[\s*\{\{\s*\"input\"\s*:\s*\"AAA\"\s*,\s*\"output\"\s*:\s*\"BBB\"\s*\}\}\s*\]"
    match = re.search(pattern, user_prompt)
    return match is not None

def save_data_to_json(data: list[dict], output_path: str):
    """
    Save a list of dictionaries to a JSON file.

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
