from .base_generator import BaseGenerator

class AnswerGenerator(BaseGenerator):
    def __init__(self, model):
        """
        初始化答案生成器

        :param model: 用于生成数据的模型接口
        """
        super().__init__(model)

    def generate(self, prompt: str) -> str:
        """
        使用模型生成答案

        :param prompt: 提供给模型的提示文本（通常是问题）
        :return: 生成的答案
        """
        answer_prompt = f"Provide an answer to the following question: {prompt}"
        return self.model.call(answer_prompt, max_tokens=100, temperature=0.7)
