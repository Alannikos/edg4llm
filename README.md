# EDG4LLM

<div align="center">

![welcome](assets/welcome.png)
<!-- ```
      __      __  __        __   ___  __     __  __   __                     
|  | |_  |   /   /  \ |\/| |_     |  /  \   |_  |  \ / _   |__| |   |   |\/| 
|/\| |__ |__ \__ \__/ |  | |__    |  \__/   |__ |__/ \__)     | |__ |__ |  | 
                                                                             
``` -->


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
[![PyPI - Downloads](https://img.shields.io/pypi/dm/edg4llm?color=blue&logo=pypi&logoColor=gold)](https://pypistats.org/packages/edg4llm)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edg4llm?logo=python&logoColor=gold)](https://pypi.org/project/edg4llm/)
</div>


**Easy Data Generation For Large Language Model(abbreviated as  EDG4LLM)**, A unified tool to generate fine-tuning datasets for LLMs, including questions, answers, and dialogues.


## Latest News

<details open>
<summary><b>2025</b></summary>

- [2025/01/28] 🚀🎉 We've added support for **DeepSeek-R1** and **InternLM3** models: the release of edg4llm [**v1.0.18**](https://pypi.org/project/edg4llm/1.0.18/). Stay tuned for more updates!
- [2025/01/12] 📢📺 We've released a project introduction video! You can find the video on [Bilibili](https://www.bilibili.com/video/BV1MccVeyEHp/). If you like it, don't forget to give it a thumbs up 👍 and follow us!
- [2025/01/11] 👋👋 We are excited to announce [**the initial release of edg4llm v1.0.12**](https://pypi.org/project/edg4llm/1.0.12/), marking the completion of its core functionalities. 

</details>

## Table of Contents
- [Latest News](#latest-news)
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Future Development Plans](#future-development-plans)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Contact me](#contact-me)
- [Star History](#star-history)

## Introduction
**edg4llm** is a Python library designed specifically for generating fine-tuning data using large language models. This tool aims to assist users in creating high-quality training datasets efficiently. At its current stage, it mainly supports text data generation. The generated data includes, but is not limited to:
- **Question data**
- **Answer data**
- **Dialogue data**

With **edg4llm**, users can easily produce diverse datasets tailored to fine-tuning requirements, significantly enhancing the performance of large language models in specific tasks.
## Features
EDG4LLM is a unified tool designed to simplify and accelerate the creation of fine-tuning datasets for large language models. With a focus on usability, efficiency, and adaptability, it offers a range of features to meet diverse development needs while ensuring seamless integration and robust debugging support.

1. **Simple to Use**: Provides a straightforward interface that allows users to get started without complex configurations.
2. **Lightweight**: Minimal dependencies and low resource consumption make it efficient and easy to use.
3. **Flexibility**: Supports a variety of data formats and generation options, allowing customization to meet specific needs.
4. **Compatibility**: Seamlessly integrates with mainstream large language models and is suitable for various development scenarios.
5. **Transparent Debugging**: Provides clear and detailed log outputs, making it easy to debug and trace issues effectively.

## Installation
To install **edg4llm**, simply run the following command in your terminal:


```bash
pip install edg4llm
```

### Supported Python Versions
- **Supported Python Versions**: Python 3.8 or higher is required for compatibility with this library. Ensure your environment meets this version requirement.

### Supported LLM Provider
The current version of edg4llm supports the following large language model providers:
- [**InternLM**](https://github.com/InternLM)
    - Developer: Developed by the Shanghai Artificial Intelligence Laboratory.
    - Advantages: InternLM is a series of open-source large language models that offer outstanding reasoning, long-text processing, and tool usage capabilities. 

- [**ChatGLM**](https://github.com/THUDM/)
    - Developer: Jointly developed by Tsinghua University and Zhipu AI.
    - Advantages: ChatGLM is an open-source, bilingual dialog language model based on the General Language Model (GLM) architecture. It has been trained on a large corpus of Chinese and English text, making it highly effective for generating natural and contextually relevant responses.
- [**DeepSeek**](https://github.com/deepseek-ai/)
    - Developer: Developed by the DeepSeek team.
    - Advantages: DeepSeek-V3 is a powerful and cost-effective open-source large language model. It offers top-tier performance, especially in tasks like language generation, question answering, and dialog systems.
- [**OpenAI ChatGPT**](https://chatgpt.com/)
    - Developer: Developed by OpenAI.
    - Advantages: OpenAI's ChatGPT is a highly advanced language model known for its robust text generation capabilities. It has been trained on a vast amount of data, allowing it to generate high-quality and contextually relevant responses. 

More providers will be added in future updates to extend compatibility and functionality. 

| **Model**         | **Free**         | **Base URL**                                               | **Model Provider** |
|--------------------|------------------|------------------------------------------------------------|--------------------|
| **InternLM**       | Yes(Partly)       | `https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions` | `internlm` |
| **ChatGLM**        | Yes(Partly)       | `https://open.bigmodel.cn/api/paas/v4/chat/completions/`   | `chatglm`  |
| **DeepSeek**       | Yes(Free Trial for New Users) | `https://api.deepseek.com/chat/completions` | `deepseek` |
| **OpenAI ChatGPT** | No (Paid Plans)   | `https://api.openai.com/v1/chat/completions`               | `chatgpt`   |


## Quick Start
To get started with **edg4llm**, follow the steps below. These examples demonstrate how to use the library to generate dialogue data based on a specific prompt.

### **Attention!**

If you want to use `question` mode, please assure that your user_prompt contains the following format:

```json
[
    {
        "question": "AAA"
    }
]
```

If you want to use `answer` mode, please assure that your user_prompt contains the following format:

```json
[
    {
        "answer": "AAA"
    }
]
```

If you want to use `dialogue` mode, please assure that your user_prompt contains the following format:

```json
[
    {{
        "input":"AAA","output":"BBB" 
    }}
]
```

### Prerequisites

1. Install the **edg4llm** package:
```bash
   pip install edg4llm
```

2. Ensure you have Python version 3.8 or higher.

3. Obtain the necessary API key and base URL for your chosen model provider (e.g., ChatGLM).

4. you can use the CLI to list the supported model_providers and model_names

```
usage: edg4llm-cli [-h] [--list-providers] [--list-models PROVIDER]

View the list of supported models.

options:
  -h, --help            show this help message and exit
  --list-providers      List all supported providers.
  --list-models PROVIDER
                        View the list of models for a specific provider.
```

### Code Example(Chinese Version)
```python
# chatglm_demo.py

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
### Code Example(English Version)
```python
# chatglm_demo.py

import edg4llm
print(edg4llm.__version__)

from edg4llm import EDG4LLM

api_key = "xxx"
base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

edg = EDG4LLM(model_provider='chatglm', model_name="glm-4-flash", base_url=base_url, api_key=api_key)

# Set the test data
system_prompt = """You are a master of ancient Chinese literature, specializing in classical poetry."""

user_prompt = """
    Goal: 1. Please generate a multi-turn dialogue set in the context of celebrating the Lunar New Year.
          2. The questions should be diverse.
          3. The dialogue should align with natural human conversational habits.
          4. Strictly follow this rule: Please return the generated data in the following format, only in JSON format. JSON template:  
                [
                    {{
                        "input":"AAA","output":"BBB" 
                    }}
                ]
                Where the input field represents a person's dialogue, and the output field represents the expert's response.
"""
num_samples = 1  # Generate only one dialogue sample

# Call the generate method to generate the dialogue
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
4. Data Generation: Use the generate method with the following parameters:
    - task_type: Defines the type of task.
        - dialogue: generate the question-answer pairs according to the prompt.
        - question: generate the question data according to the prompt.
        - answer: generate the answer data according to the questions and the prompt.
        
    - system_prompt and user_prompt: Provide context and task-specific instructions.
    - num_samples: Specifies how many samples to generate.
5. Output: The generated data is returned as a JSON object in the specified format.

## Requirements
This project has **minimal dependencies**, requiring only the requests library. Make sure to have the following version installed:

- requests>=2.32.3

## Future Development Plans
1. - [ × ] Recording Introduction Video
2. - [ ] Support Gemini2
3. - [ ] Support local large language models
4. - [ ] Support other types of data, such as picture.
5. - [ ] preprocess the base_url and api_key

## Acknowledgments
| Project | Description |
|---|---|
| [FunGPT](https://github.com/Alannikos/FunGPT) | An open-source Role-Play project |
| [InternLM](https://github.com/InternLM/InternLM) | A series of advanced open-source large language models |
| [ChatGLM](https://github.com/THUDM/) | A bilingual dialog language model based on the General Language Model (GLM) architecture, jointly developed by Tsinghua University and Zhipu AI. |
| [DeepSeek](https://github.com/deepseek-ai/) | A powerful and cost-effective open-source large language model, excelling in tasks such as language generation, question answering, and dialog systems. |
| [ChatGPT](https://openai.com/chatgpt/) | A highly advanced language model developed by OpenAI, known for its robust text generation capabilities. |

## License
MIT License - See [LICENSE](LICENSE) for details.

## Contact Me
Thank you for using **EDG4LLM**! Your support and feedback are invaluable in making this project better.

If you encounter any issues, have suggestions, or simply want to share your thoughts, feel free to:
- Submit an Issue: Visit the [Issues Page](https://github.com/Alannikos/edg4llm/issues) and describe the problem or suggestion.
- Email Me: You can also reach out directly via email at alannikos768@outlook.com. I'll do my best to respond promptly.

Your contributions and feedback are greatly appreciated. Thank you for helping improve this tool!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Alannikos/edg4llm&type=Date)](https://star-history.com/#Alannikos/edg4llm&Date)