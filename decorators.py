"""
This is a file which contains decorators
"""
from functools import wraps
import logging


def log_parameters(func):
    """
    Decorator that logs the input and output parameters of a method.

    Args:
        func (callable): The method being decorated.

    Returns:
        callable: The decorated method.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that logs the input and output parameters.

        Args:
            *args: The positional arguments passed to the method.
            **kwargs: The keyword arguments passed to the method.

        Returns:
            Any: The result of the method call.
        """
        print(f"Calling method '{func.__name__}' with arguments:")
        print(f"  - args: {args}")
        print(f"  - kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Method '{func.__name__}' returned: {result}")
        return result

    return wrapper


def print_iterable_length(func):
    """
    Decorator that prints the length of the iterable returned by a method.

    Args:
        func (callable): The method being decorated.

    Returns:
        callable: The decorated method.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that prints the length of the iterable returned by the method.

        Args:
            *args: The positional arguments passed to the method.
            **kwargs: The keyword arguments passed to the method.

        Returns:
            Any: The result of the method call.
        """
        result = func(*args, **kwargs)

        if hasattr(result, "__iter__"):
            length = len(result)
        else:
            length = 1

        print(f"The iterable returned from method '{func.__name__}' has a length of: {length}")
        return result

    return wrapper


def logged(exception, mode):
    """
    A parameterized decorator that logs exceptions using the logging module based on the specified mode.

    Args:
        exception (Exception): The exception type to be caught and logged.
        mode (str): The logging mode, either "console" or "file".

    Returns:
        function: The decorated function.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            The wrapper function that wraps the original function and logs exceptions.

            Args:
                *args: Positional arguments passed to the wrapped function.
                **kwargs: Keyword arguments passed to the wrapped function.

            Returns:
                Any: The return value of the wrapped function.

            Raises:
                Exception: The original exception raised by the wrapped function.

            """

            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    console_handler = logging.StreamHandler()
                    logger.addHandler(console_handler)
                elif mode == "file":
                    file_handler = logging.FileHandler("exception_logger.txt")
                    logger.addHandler(file_handler)
                logger.exception(str(e))

        return wrapper

    return decorator
