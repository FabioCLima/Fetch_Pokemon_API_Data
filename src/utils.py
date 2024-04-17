'''
This module will have some functions can be helper to the entry point
to the project, but the project can run without.

'''
import time
from functools import wraps
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    '''
    Decorator to measure the execution time of a function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        '''
        Wrapper function to measure the execution time of the decorated
        function.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            Any: The result of the decorated function.
        '''
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the decorated function
        end_time = time.time()  # End time
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__!r} took {elapsed_time:.4f} sec")
        return result

    return wrapper


"""
# Example of decoration applied to a function
@timer
def example_function(n: int) -> str:
    '''
    Example function to demonstrate the timer decorator.

    Args:
        n (int): The upper limit for the sum.

    Returns:
        str: The result string.
    '''
    return f"The sum is {sum(range(n))}"
"""
