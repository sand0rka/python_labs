"""
This module provides custom exception classes.
Exceptions:
    TransportNotFoundException: raised when a transport object is not found with the specified ID.
    SpeedExceededException: raised when the specified speed exceeds the maximum speed of the transport.
"""


class TransportNotFoundException(Exception):
    """
    Exception raised when a transport object is not found with the specified ID.

    Args:
        message (str): Custom error message describing the exception. Defaults to
            "no transport found with this ID".
    """

    def __init__(self, message: str = "no transport found with this ID"):
        super().__init__(message)


class SpeedExceededException(Exception):
    """
    Exception raised when the specified speed exceeds the maximum speed of the transport.

    Args:
        message (str): Custom error message describing the exception. Defaults to
            "speed exceeds the maximum speed of the transport".
    """

    def __init__(self, message: str = "speed exceeds the maximum speed of the transport"):
        super().__init__(message)
