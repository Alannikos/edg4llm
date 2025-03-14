# EDG4LLM

<div align="center">

![welcome](assets/welcome.png)
<!-- ```
      __      __  __        __   ___  __     __  __   __                     
|  | |_  |   /   /  \ |\/| |_     |  /  \   |_  |  \ / _   |__| |   |   |\/| 
|/\| |__ |__ \__ \__/ |  | |__    |  \__/   |__ |__/ \__)     | |__ |__ |  | 
                                                                             
``` -->

  [English](README_en.md) | [简体中文](README_zh.md)
</div>

<div align="center">

[📘Documentation](https://github.com/alannikos/edg4llm) |
[🛠️Quick Start](https://github.com/alannikos/edg4llm) |
[🤔Reporting Issues](https://github.com/alannikos/edg4llm/issues) 

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


**EDG4LLM（Easy Data Generation For Large Language Model）** ，一个用于生成大型语言模型微调数据集的统一工具，现阶段支持生成问题、答案和对话。

## 最新动态

<details open>
<summary><b>2025</b></summary>

- [2025/01/28] 🚀🎉 新增对 **DeepSeek-R1** 和 **InternLM3** 模型的支持，edg4llm [**v1.0.18**](https://pypi.org/project/edg4llm/1.0.18/) 版本现已发布。敬请期待更多更新！
- [2025/01/12] 📢📺 发布项目介绍视频！你可以在 [Bilibili](https://www.bilibili.com/video/BV1MccVeyEHp/) 上找到该视频。如果你喜欢的话，别忘了点个赞 👍 并关注**Alannikos**哦！
- [2025/01/11] 👋👋 **edg4llm** 的初始版本 [**v1.0.12**](https://pypi.org/project/edg4llm/1.0.12/) 正式发布，标志着其核心功能已经完成。

</details>

## 目录
- [最新动态](#最新动态)
- [项目简介](#项目简介)
- [项目特点](#项目特点)
- [Python库安装](#Python库安装)
- [快速上手](#快速上手)
- [Requirements](#requirements)
- [未来开发计划](#未来开发计划)
- [致谢](#致谢)
- [License](#license)
- [联系方式](#联系方式)
- [Star History](#star-history)

## 项目简介
**edg4llm** 是一个专为利用大型语言模型生成微调数据而设计的 Python 库。该工具旨在帮助用户高效创建高质量的训练数据集。在现阶段，它主要支持文本数据的生成。生成的数据包括但不限于：
- **问题数据**
- **答案数据**
- **对话数据**

通过使用 **edg4llm**，用户可以轻松生成针对微调需求的多样化数据集，从而显著提升大型语言模型在特定任务中的性能。
## 项目特点

EDG4LLM 是一款旨在简化和加速大型语言模型微调数据集创建的统一工具。具有易用性、高效性和适应性的特性，它提供了一系列功能以满足多样化的开发需求，同时确保无缝集成和强大的调试支持。

1. **简单易用**：提供简单直观的接口，用户无需复杂配置即可快速上手。
2. **轻量化**：依赖极少，资源消耗低，使用高效便捷。
3. **灵活性**：支持多种数据格式和生成选项，可根据特定需求进行定制。
4. **兼容性**：与主流大型语言模型无缝集成，适用于各种开发场景。
5. **透明调试**：提供清晰详尽的日志输出，便于有效调试和问题追踪。

## Python库安装

要安装 **edg4llm**，只需在终端中运行以下命令：


```bash
pip install edg4llm
```

### 支持的 Python 版本
- **支持的 Python 版本**：需要 Python 3.8 或更高版本才能与此库兼容。请确保您的环境满足此版本要求。

### 支持的大型语言模型提供商
当前版本的 edg4llm 支持以下大型语言模型提供商：

- [**InternLM**](https://github.com/InternLM)
    - 开发者：由上海人工智能实验室开发。
    - 优势：InternLM 是一系列开源大型语言模型，具有出色的推理能力、长文本处理能力和工具使用能力。

- [**ChatGLM**](https://github.com/THUDM/)
    - 开发者：由清华大学和智谱 AI 联合开发。
    - 优势：ChatGLM 是一个基于通用语言模型（GLM）架构的开源双语对话语言模型。它在大量中英文文本上进行了训练，能够生成自然且上下文相关的响应，效果极佳。

- [**DeepSeek**](https://github.com/deepseek-ai/)
    - 开发者：由 DeepSeek 团队开发。
    - 优势：DeepSeek-V3 是一款性能强大且经济高效的开源大型语言模型，在语言生成、问答和对话系统等任务中表现出色。

- [**OpenAI ChatGPT**](https://chatgpt.com/)
    - 开发者：由 OpenAI 开发。
    - 优势：OpenAI 的 ChatGPT 是一款高度先进的语言模型，以其强大的文本生成能力而闻名。它经过海量数据训练，能够生成高质量且上下文相关的响应。

未来更新中将添加更多提供商，以扩展兼容性和功能性。

| **模型**         | **是否免费**         | **base_url**                                               | **Model Provider** |
|--------------------|------------------|------------------------------------------------------------|----------------|
| **InternLM**       | 部分免费          | `https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions` | `internlm`     |
| **ChatGLM**        | 部分免费          | `https://open.bigmodel.cn/api/paas/v4/chat/completions/`   | `chatglm`      |
| **DeepSeek**       | 新用户免费试用    | `https://api.deepseek.com/chat/completions`                | `deepseek`     |
| **OpenAI ChatGPT** | 付费（无免费）| `https://api.openai.com/v1/chat/completions`               | `chatgpt`      |

## 快速上手

要开始使用 **edg4llm**，请按照以下步骤操作。这些示例演示了如何使用该库根据特定提示生成微调数据。

### **注意！**

如果您想使用 `question` 模式，请确保您的 `user_prompt` 包含以下格式：

```json
[
    {
        "question": "AAA"
    }
]
```

如果您想使用 `answer` 模式，请确保您的 `user_prompt` 包含以下格式：

```json
[
    {
        "answer": "AAA"
    }
]
```

如果您想使用 `dialogue` 模式，请确保您的 `user_prompt` 包含以下格式：

```json
[
    {{
        "input":"AAA","output":"BBB" 
    }}
]
```

### 前置条件

1. 安装 **edg4llm** 包：
```bash
   pip install edg4llm
```

2. 确保您的 Python 版本为 3.8 或更高。

3. 获取所选模型提供商（例如 ChatGLM）所需的 API 密钥和基础 URL。

4. 您可以使用 CLI 列出支持的模型提供商和模型名称：

```
用法: edg4llm-cli [-h] [--list-providers] [--list-models PROVIDER]

查看支持的模型列表。

选项:
  -h, --help            显示帮助信息并退出
  --list-providers      列出所有支持的提供商。
  --list-models PROVIDER
                        查看特定提供商的模型列表。
```

### 示例代码（中文版本）
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

### 示例代码（英文版本）
```python
# chatglm_demo.py

import edg4llm
print(edg4llm.__version__)

from edg4llm import EDG4LLM

api_key = "xxx"
base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

edg = EDG4LLM(model_provider='chatglm', model_name="glm-4-flash", base_url=base_url, api_key=api_key)

# 设置测试数据
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

### 说明

1. **导入库**：导入 `edg4llm` 库，并通过 `print(edg4llm.__version__)` 验证版本。

2. **初始化**：使用 `EDG4LLM` 初始化库，传入正确的model_provider、model_name、base_url 和 api_key。

3. **prompt参数**：
    - `system_prompt` 定义助手的行为或角色。
    - `user_prompt` 提供生成数据的具体指令。

4. **数据生成**：使用 `generate` 方法，参数如下：
    - `task_type`：定义任务类型。
        - `dialogue`：根据提示生成问答对。
        - `question`：根据提示生成问题数据。
        - `answer`：根据问题和提示生成答案数据。
    - `system_prompt` 和 `user_prompt`：提供上下文和任务特定的指令。
    - `num_samples`(可选)：指定生成的样本数量。

5. **输出**：生成的数据以指定的 JSON 格式返回。

## Requirements

该项目的**依赖项极少**，仅需安装 `requests` 库。请确保安装了以下版本：

- requests>=2.32.3

## 未来开发计划
1. - [ × ] 录制介绍视频
2. - [ ] 支持 Gemini2
3. - [ ] 支持本地大型语言模型
4. - [ ] 支持其他类型的数据，例如图片
5. - [ ] 预处理 base_url 和 api_key

## 致谢
| Project | Description |
|---|---|
| [FunGPT](https://github.com/Alannikos/FunGPT) | An open-source Role-Play project |
| [InternLM](https://github.com/InternLM/InternLM) | A series of advanced open-source large language models |
| [ChatGLM](https://github.com/THUDM/) | A bilingual dialog language model based on the General Language Model (GLM) architecture, jointly developed by Tsinghua University and Zhipu AI. |
| [DeepSeek](https://github.com/deepseek-ai/) | A powerful and cost-effective open-source large language model, excelling in tasks such as language generation, question answering, and dialog systems. |
| [ChatGPT](https://openai.com/chatgpt/) | A highly advanced language model developed by OpenAI, known for its robust text generation capabilities. |

## License
MIT License - See [LICENSE](LICENSE) for details.

## 联系方式
感谢您使用 **EDG4LLM**！您的支持和反馈对于改进这个项目至关重要。

如果您遇到任何问题、有建议，或者只是想分享您的想法，请随时：
- 提交问题：访问 [issues页面](https://github.com/Alannikos/edg4llm/issues) 并描述您遇到的问题或建议。
- 发送邮件：您也可以通过电子邮件直接联系我，邮箱地址为 alannikos768@outlook.com。我会尽力及时回复您。

您的贡献和反馈对我们非常重要。感谢您帮助改进这个工具！

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Alannikos/edg4llm&type=Date)](https://star-history.com/#Alannikos/edg4llm&Date)