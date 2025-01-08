from edg4llm.models.chatgpt import OpenAIModel  # 假设你已经实现了 OpenAIModel

class DataGenerator:
    def __init__(self, model_type: str, api_key: str):
        """
        初始化数据生成器
        
        :param model_type: 使用的模型类型（例如：openai）
        :param api_key: 用于身份验证的 API 密钥
        """
        if model_type == "openai":
            self.model = OpenAIModel(api_key)  # 根据模型类型选择不同的模型
        else:
            raise ValueError("Unsupported model type")

    def generate_question(self, prompt: str) -> str:
        """
        生成问题数据
        
        :param prompt: 用于生成问题的提示文本
        :return: 生成的问题
        """
        return self.model.call(prompt, max_tokens=50, temperature=0.7)

    def generate_answer(self, question: str) -> str:
        """
        生成答案数据
        
        :param question: 用于生成答案的问题
        :return: 生成的答案
        """
        prompt = f"Answer the following question: {question}"
        return self.model.call(prompt, max_tokens=100, temperature=0.7)

    def generate_dialogue(self, user_input: str) -> str:
        """
        生成对话数据

        :param user_input: 用户输入的对话内容
        :return: 生成的对话内容
        """
        prompt = f"User: {user_input}\nBot:"
        return self.model.call(prompt, max_tokens=100, temperature=0.7)
