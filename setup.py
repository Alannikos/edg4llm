from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="edg4llm",  # 项目名称
    version="1.0.18",  # 项目版本
    author="Alannikos",  # 作者姓名
    author_email="alannikos768@outlook.com",  # 作者邮箱
    description="A unified tool to generate fine-tuning datasets for LLMs, including questions, answers, and dialogues.",  # 简短描述
    long_description=long_description,  # 长描述
    long_description_content_type="text/markdown",  # 长描述格式
    url="https://github.com/alannikos/edg4llm",  # 项目主页（GitHub 或其他）
    packages=find_packages(include=["edg4llm", "edg4llm.*"]),  # 自动发现包含的模块
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 选择的许可证类型
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",  # Python 版本要求
    install_requires=[
        "requests>=2.32.3"
    ],
    include_package_data=True,  # 包含非代码文件，如配置文件
    zip_safe=False,  # 是否以 zip 格式分发（通常为 False）
    keywords="LLM fine-tuning data-generation AI NLP",  # 关键词
    entry_points={
        "console_scripts": [
            "edg4llm-cli=edg4llm.utils.list_supported_models:main"
        ]
    },
)
