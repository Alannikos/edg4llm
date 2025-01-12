import argparse
from edg4llm.utils.logger import custom_logger

class ModelManager:
    """
    A class to manage supported model providers and their models.

    Attributes
    ----------
    supported_models : dict
        A dictionary mapping provider names to their supported models.

    Methods
    -------
    list_providers():
        Returns a list of all supported providers.
    list_models_by_provider(provider_name):
        Returns a list of models supported by the given provider.
    """
    def __init__(self):
        """
        Initializes the ModelManager with a predefined list of supported models.
        """
        self.supported_models = {
            "ChatGLM": ["glm-4-plus", "glm-4-0520", "glm-4-air", "glm-4-airx", "glm-4-long", "glm-4-flashx", "glm-4-flash"],
            "DeepSeek": ["deepseek-chat"],
            "InternLM": ["internlm2.5-latest"],
            "ChatGPT": ["gpt-3.5-turbo-16k", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-0125", "gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-mini-2024-07-18", "o1-mini", "o1-mini-2024-09-12", "o1-preview","o1-preview-2024-09-12"]
        }

    def list_providers(self):
        """
        Lists all supported model providers.

        Returns
        -------
        list
            A list of provider names.
        """
        return list(self.supported_models.keys())

    def list_models_by_provider(self, provider_name):
        """
        Lists all models supported by a given provider.

        Parameters
        ----------
        provider_name : str
            The name of the provider.

        Returns
        -------
        list or None
            A list of model names supported by the provider,
            or None if the provider does not exist.
        """
        return self.supported_models.get(provider_name, None)

def main():
    """
    Entry point of the script to display supported model providers
    and their corresponding models based on the user's input.
    """
    parser = argparse.ArgumentParser(description="View the list of supported models.")
    parser.add_argument("--list-providers", action="store_true", help="List all supported providers.")
    parser.add_argument("--list-models", type=str, metavar="PROVIDER", help="View the list of models for a specific provider.")

    args = parser.parse_args()

    manager = ModelManager()

    if args.list_providers:
        providers = manager.list_providers()
        print("Supported model providers:")
        for provider in providers:
            print(f"  - {provider}")
    elif args.list_models:
        models = manager.list_models_by_provider(args.list_models)
        if models:
            print(f"{args.list_models} supports the following models:")
            for model in models:
                print(f"  - {model}")
        else:
            print(f"Provider '{args.list_models}' does not exist or is not supported.")
    else:
        parser.print_help()

