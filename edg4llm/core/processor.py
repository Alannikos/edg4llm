import json

from edg4llm.utils.logger import custom_logger

logger = custom_logger("process", "INFO")

class DataProcessor:
    def __init__(self):
        pass

    def process(self, data: str) -> dict:
        """
        处理生成的数据
        
        :param data: 生成的文本数据
        :return: 格式化后的数据
        """
        pass

    def postprocessing(self, conversation_data, system_prompt: str = None):
        # 数据后处理
        try:
            conversation_data = json.loads(conversation_data.replace("```json","").replace("```",""))
        except Exception  as exception:
            logger.error("解析json异常:%s, 内容：%s",str(exception), conversation_data.choices[0].message.content)
            return None

        result = {"conversation": []}
        
        for idx, data in enumerate(conversation_data):
            if idx == 0:
                data['system'] = system_prompt if system_prompt is not None else ""
            result["conversation"].append(data)

        return result

    def save_dialogue_to_jsonl(self, data):
        """
        这里要修改一下路径问题
        """
        with open('1.jsonl', 'w', encoding='utf-8') as f:

            json.dump(data, f, ensure_ascii=False, indent=4)

