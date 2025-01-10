from dataclasses import dataclass

@dataclass
class Template:
    """
    A class to define language-specific templates for user prompts, providing a strict JSON format 
    to preprocess user input. If the user's prompt does not include format instructions, the 
    appropriate template will be added to enforce the required structure.

    Attributes:
    ----------
    question_zh_template : str
        A JSON format template for Chinese question prompts. Ensures that generated questions 
        are returned in a JSON format with a "question" field.

    answer_zh_template : str
        A JSON format template for Chinese answer prompts. Ensures that generated answers 
        are returned in a JSON format with an "answer" field.

    dialogue_zh_template : str
        A JSON format template for Chinese dialogue prompts. Ensures that the interaction is 
        returned in a JSON format with "input" representing the question and "output" representing 
        the response.

    question_en_template : str
        A JSON format template for English question prompts. Ensures that generated questions 
        are returned in a JSON format with a "question" field.

    answer_en_template : str
        A JSON format template for English answer prompts. Ensures that generated answers 
        are returned in a JSON format with an "answer" field.

    dialogue_en_template : str
        A JSON format template for English dialogue prompts. Ensures that the interaction is 
        returned in a JSON format with "input" representing the question and "output" representing 
        the response.
    
    Notes:
    -----
    This class is designed for preprocessing user prompts. If a user's input does not include 
    specific format instructions, the appropriate template (based on language) is appended to 
    the user prompt to ensure compliance with the required JSON format.
    """

    question_zh_template = \
        """
            严格遵循规则: 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                            [
                                {
                                    "question":"AAA"
                                }
                            ]
                            其中question字段表示生成的问题
        """

    answer_zh_template = \
        """
            严格遵循规则: 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                            [
                                {
                                    "answer":"AAA"
                                }
                            ]
                            其中answer字段表示生成的答案
        """

    dialogue_zh_template = \
        """
            严格遵循规则: 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                            [
                                {{
                                    "input":"AAA","output":"BBB" 
                                }}
                            ]
                            其中input字段表示问题, output字段回答
        """

    question_en_template = \
        """
            Strictly follow the rules: Please return the generated data in the following format, 
            only in JSON format. JSON template:  
                            [
                                {
                                    "question":"AAA"
                                }
                            ]
                            The "question" field represents the generated question.
        """

    answer_en_template = \
        """
            Strictly follow the rules: Please return the generated data in the following format, 
            only in JSON format. JSON template:  
                            [
                                {
                                    "answer":"AAA"
                                }
                            ]
                            The "answer" field represents the generated answer.
        """

    dialogue_en_template = \
        """
            Strictly follow the rules: Please return the generated data in the following format, 
            only in JSON format. JSON template:  
                            [
                                {{
                                    "input":"AAA","output":"BBB" 
                                }}
                            ]
                            The "input" field represents the question, and the "output" field 
                            represents the answer.
        """
