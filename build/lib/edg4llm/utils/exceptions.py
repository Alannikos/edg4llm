from typing import Optional


class HttpClientError(Exception):
    """
    Exception raised for errors encountered in the HTTP client.

    Parameters
    ----------
    message : str
        A detailed error message describing the issue.
    status_code : Optional[int], optional
        The HTTP status code associated with the error, by default None.

    Attributes
    ----------
    status_code : Optional[int]
        The HTTP status code associated with the error.
    """

    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class InvalidPromptError(Exception):
    """
    Custom exception raised when an invalid or empty prompt is encountered.

    Notes
    -----
    This exception is intended to handle cases where a required prompt input
    is missing or invalid.
    """
    pass
