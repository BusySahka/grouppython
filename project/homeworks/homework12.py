from typing import Callable
from functools import wraps


def round_result(ndigits: int):
    def decorator(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return round(result, ndigits)
            return result
        return inner
    return decorator


@round_result(2)
def divide(a, b):
    return a / b

print(divide(10, 3))   # 3.33
print(divide(5, 2))    # 2.5
print(divide(1, 4))    # 0.25
