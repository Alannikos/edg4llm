from .base_generator import BaseGenerator

class QuestionGenerator(BaseGenerator):
    def __init__(self, model):
        """
        初始化问题生成器

        :param model: 用于生成数据的模型接口
        """
        super().__init__(model)

    def generate(self, prompt: str) -> str:
        """
        使用模型生成问题

        :param prompt: 提供给模型的提示文本
        :return: 生成的问题
        """
        question_prompt = f"Generate a question based on the following text: {prompt}"
        return self.model.call(question_prompt, max_tokens=50, temperature=0.7)
