import os
from typing import Any, Tuple, Dict


from edg4llm.core.pipeline import DataPipeline



"""
{
  "instruction": "Explain the theory of relativity in simple terms.",
  "input": "",
  "output": "The theory of relativity, proposed by Einstein"
}
"""


class Edg4LLM:
    def __init__(self
                , model_type: str = "chatglm"
                , base_url: str = None
                , api_key: str = None
                ):

        self._pConfig = {
            "model_type" : model_type
            , "base_url": base_url
            , "api_key" : api_key
        }

        self.pipeline = DataPipeline(self._pConfig)

    def generate(self
                , task_type: str = 'dialogue'
                , system_prompt: str = None
                , user_prompt: str = None
                , do_sample: bool = True
                , temperature: float = 0.95
                , top_p: float = 0.7
                , max_tokens: int = 4095
                , num_samples: int = 10
                , output_format: str = "alpaca"
                ):
        """
        生成数据的统一方法。
        :param task_type: 任务类型，例如 'question', 'answer', 'dialogue'
        :param system_prompt: 生成数据的主题（可选）
        :param user_prompt: 生成数据的主题（可选）
        :param num_samples: 生成数据的数量
        :param output_format: 输出数据的格式，例如 'json', 'list'
        :return: 生成的数据
        """

        data = self._generate(task_type, system_prompt, user_prompt, do_sample, temperature, top_p, max_tokens, num_samples, output_format)
        return data

    def _generate(self
                , task_type: str = 'dialogue'
                , system_prompt: str = None
                , user_prompt: str = None
                , do_sample: bool = True
                , temperature: float = 0.95
                , top_p: float = 0.7
                , max_tokens: int = 4095
                , num_samples: int = 10
                , output_format: str = "alpaca"
                ):

        self._tConfig = {
            "task_type" : task_type
            , "system_prompt" : system_prompt
            , "user_prompt" : user_prompt
            , "do_sample" : do_sample
            , "temperature" : temperature
            , "top_p" : top_p
            , "max_tokens" : max_tokens
            , "num_samples" : num_samples
            , "output_format" : output_format
        }
    
        data = self.pipeline.generate_data(self._tConfig)

        return data