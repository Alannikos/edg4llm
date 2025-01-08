from .base_generator import BaseGenerator

class DialogueGenerator(BaseGenerator):
    def __init__(self, model):
        """
        初始化对话生成器

        :param model: 用于生成数据的模型接口
        """
        super().__init__(model)

    def generate(self, prompt: str) -> str:
        """
        使用模型生成对话对

        :param prompt: 用户输入的对话内容
        :return: 生成的对话内容
        """
        dialogue_prompt = f"User: {prompt}\nBot:"
        return self.model.call(dialogue_prompt, max_tokens=150, temperature=0.7)
