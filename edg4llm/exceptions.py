from typing import Optional


class HttpClientError(Exception):
    """Exception raised for errors in the HTTP client."""
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class InvalidPromptError(Exception):
    """自定义异常类，用于处理空的 prompt"""
    pass

