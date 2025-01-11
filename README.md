# EDG4LLM

<div align="center">

![welcome](assets/welcome.png)

</div>

<div align="center">

[📘Documentation](https://github.com/Alannikos/FunGPT) |
[🛠️Quick Start](https://github.com/Alannikos/FunGPT) |
[🤔Reporting Issues](https://github.com/Alannikos/FunGPT/issues) 

</div>

<div align="center">

<!-- PROJECT SHIELDS -->
[![GitHub Issues](https://img.shields.io/github/issues/Alannikos/edg4llm?style=flat&logo=github&color=%23FF5252)](https://github.com/Alannikos/edg4llm/issues)
[![GitHub forks](https://img.shields.io/github/forks/Alannikos/edg4llm?style=flat&logo=github&color=%23FF9800)](https://github.com/Alannikos/edg4llm/forks)
![GitHub Repo stars](https://img.shields.io/github/stars/Alannikos/edg4llm?style=flat&logo=github&color=%23FFEB3B)
![GitHub License](https://img.shields.io/github/license/Alannikos/edg4llm?style=flat&logo=github&color=%234CAF50)
[![Discord](https://img.shields.io/discord/1327445853388144681?style=flat&logo=discord)](https://discord.com/channels/1327445853388144681/)
[![Bilibili](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D3494365446015137&query=%24.data.follower&style=flat&logo=bilibili&label=followers&color=%23FF69B4)](https://space.bilibili.com/3494365446015137)
[![PyPI - Version](https://img.shields.io/pypi/v/edg4llm?style=flat&logo=pypi&logoColor=blue&color=red)](https://pypi.org/project/edg4llm/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/edg4llm?color=blue&logo=pypi&logoColor=gold)](https://pypi.org/project/edg4llm/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edg4llm?logo=python&logoColor=gold)](https://pypi.org/project/edg4llm/)
</div>



Easy Data Generation For Large Language Model, A unified tool to generate fine-tuning datasets for LLMs, including questions, answers, and dialogues.


## Table of Contents
- [Latest News](#latest-news)
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [License](#license)
- [Future Development Plans](#future-development-plans)
- [Acknowledgments](#acknowledgments)
- [Disclaimer](#disclaimer)

## Latest News

<details open>
<summary><b>2025</b></summary>

- [2025/01/11] 👋👋 

</details>

## Introduction
$\quad$ edg4llm is a Python library designed specifically for generating fine-tuning data using large language models. This tool aims to assist users in creating high-quality training datasets efficiently. At its current stage, it mainly supports text data generation. The generated data includes, but is not limited to:
- **Question data**
- **Answer data**
- **Dialogue data**

$\quad$ With edg4llm, users can easily produce diverse datasets tailored to fine-tuning requirements, significantly enhancing the performance of large language models in specific tasks.
## Features

1. **Simple to Use**: Provides a straightforward interface that allows users to get started without complex configurations.
2. **Lightweight**: Minimal dependencies and low resource consumption make it efficient and easy to use.
3. **High Efficiency**: Utilizes an optimized generation mechanism to quickly produce large volumes of high-quality fine-tuning data.
4. **Flexibility**: Supports a variety of data formats and generation options, allowing customization to meet specific needs.
Compatibility: Seamlessly integrates with mainstream large language models and is suitable for various development scenarios.

## Installation

```bash
pip install edg4llm
```

### Supported Python Versions
- Python >= 3.8

### LLM Provider

- ChatGLM
- DeepSeek
- OpenAI ChatGPT
- InternLM

## Quick Start

```python
import edg4llm
print(edg4llm.__version__)

from edg4llm import EDG4LLM

api_key = "xxx"
base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

edg = EDG4LLM(model_provider='chatglm', model_name="glm-4-flash", base_url=base_url, api_key=api_key)
# 设置测试数据
system_prompt = """你是一个精通中国古代诗词的古文学大师"""

user_prompt = """
    目标: 1. 请生成过年为场景的连续多轮对话记录
            2. 提出的问题要多样化。
            3. 要符合人类的说话习惯。
            4. 严格遵循规则: 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                [
                    {{
                        "input":"AAA","output":"BBB" 
                    }}
                ]
                其中input字段表示一个人的话语, output字段表示专家的话语
"""
num_samples = 1  # 只生成一个对话样本

# 调用 generate 方法生成对话
data_dialogue = edg.generate(
    task_type="dialogue",
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    num_samples=num_samples
)
```

## Requirements

## License
MIT License - See [LICENSE](LICENSE) for details.

## Future Development Plans

## Acknowledgments

## Disclaimer