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
- [License](#disclaimer)
- [Star History](#star-history)

## Latest News

<details open>
<summary><b>2025</b></summary>

- [2025/01/11] 👋👋 We are excited to announce [**the initial release of edg4llm v1.0.12**](https://pypi.org/project/edg4llm/1.0.12/), marking the completion of its core functionalities. 

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
To install **edg4llm**, simply run the following command in your terminal:


```bash
pip install edg4llm
```

### Supported Python Versions
- **Supported Python Versions**: Python 3.8 or higher is required for compatibility with this library. Ensure your environment meets this version requirement.

### LLM Provider
The current version of edg4llm supports the following large language model providers:

- **ChatGLM**: A versatile LLM optimized for various text generation tasks.
- **DeepSeek**: A powerful and efficient LLM for fine-tuned applications.
- **OpenAI ChatGPT**: The widely-used conversational AI from OpenAI.
- **InternLM**: A robust LLM tailored for enterprise and advanced use cases.

More providers will be added in future updates to extend compatibility and functionality. 


## Quick Start

To get started with **edg4llm**, follow the steps below. This example demonstrates how to use the library to generate dialogue data based on a specific prompt.

### Prerequisites

1. Install the **edg4llm** package:
```bash
   pip install edg4llm
```

2. Ensure you have Python version 3.8 or higher.
3. Obtain the necessary API key and base URL for your chosen model provider (e.g., ChatGLM).

### Code Example
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

### Explanation

1. Importing the Library: Import the edg4llm library and verify the version using print(edg4llm.__version__).

2. Initialization: Use EDG4LLM to initialize the library with the appropriate model provider, model name, base URL, and API key.

3. Prompts:
    - system_prompt defines the behavior or role of the assistant.
    - user_prompt provides specific instructions for generating data.
4. Data Generation:
Use the generate method with the following parameters:
    - task_type: Defines the type of task (e.g., dialogue, question-answering).
    - system_prompt and user_prompt: Provide context and task-specific instructions.
    - num_samples: Specifies how many samples to generate.
5. Output: The generated data is returned as a JSON object in the specified format.

## Requirements

- Only require requests

## License
MIT License - See [LICENSE](LICENSE) for details.

## Future Development Plans
1. - [ ] Recording Introduction Video
2. - [ ] Support Gemini2
3. - [ ] Support local large language models
4. - [ ] Support other types of data, such as picture.

## Acknowledgments
| Project | Description |
|---|---|
| [InternLM](https://github.com/InternLM/InternLM) | A series of advanced open-source large language models |
| [FunGPT](https://github.com/Alannikos/FunGPT) | An open-source Role-Play project |

## License
MIT License - See [LICENSE](LICENSE) for details.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Alannikos/edg4llm&type=Date)](https://star-history.com/#Alannikos/edg4llm&Date)