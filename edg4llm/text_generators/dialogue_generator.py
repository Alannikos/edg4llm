from .base_generator import BaseGenerator

class DialogueGenerator(BaseGenerator):
    def __init__(self, model):
        """
        初始化对话生成器

        :param model: 用于生成数据的模型接口
        """
        super().__init__(model)

    def generate(self, tConfig) -> list:
        """
        使用模型生成对话对

        :param prompt: 用户输入的对话内容
        :return: 生成的对话内容
        """

        # 从 tConfig 提取参数
        system_prompt = tConfig.get("system_prompt", "")
        user_prompt = tConfig.get("user_prompt", "")
        model = tConfig.get("model", "glm-4-flash")
        do_sample = tConfig.get("do_sample", True)
        temperature = tConfig.get("temperature", 0.95)
        top_p = tConfig.get("top_p", 0.7)
        max_tokens = tConfig.get("max_tokens", 4095)
        num_samples = tConfig.get("num_samples", 1)  # 默认为生成1次

        # 用于存储生成的对话数据
        dialogues = []

        # 多次生成对话数据
        for _ in range(num_samples):
            generated_dialogue = self.model.execute_request(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                model=model,
                do_sample=do_sample,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_tokens
            )

            dialogues.append(self._convert_original_to_alpaca(system_prompt, generated_dialogue))

        return dialogues
