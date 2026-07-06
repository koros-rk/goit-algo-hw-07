from functools import wraps
from typing import Callable

from errors import ValidationError


def validate_payload(schema: dict):
    def decorator(function: Callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if len(args) != len(schema):
                raise ValidationError(
                    f"Expected {', '.join(schema.keys())}. Got {len(args)} arguments"
                )

            for (key, expected_type), value in zip(schema.items(), args):
                if not isinstance(value, expected_type):
                    raise ValidationError(
                        f'"{key}" expected {expected_type.__name__}, '
                        f"got {type(value).__name__}"
                    )

            return function(*args, **kwargs)

        return wrapper

    return decorator
