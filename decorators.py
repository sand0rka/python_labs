"""
This is a file which contains decorators
"""
from functools import wraps


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
            length = sum(1 for _ in result)
        else:
            length = 1

        print(f"The iterable returned from method '{func.__name__}' has a length of: {length}")
        return result

    return wrapper
