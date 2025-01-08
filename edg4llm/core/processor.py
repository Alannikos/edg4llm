class DataProcessor:
    def __init__(self):
        pass

    def process(self, data: str) -> dict:
        """
        处理生成的数据
        
        :param data: 生成的文本数据
        :return: 格式化后的数据
        """
        # 这里可以根据需要进行清理、格式化等操作
        # 例如：去除多余的空格，确保数据符合预期格式等
        
        cleaned_data = data.strip()  # 去除首尾空白字符

        # 返回处理后的数据，假设需要格式化成一个字典（你可以根据需要更改格式）
        return {
            "finetune_data": cleaned_data
        }
