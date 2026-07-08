from functools import wraps
from typing import Callable

from errors import (
    BirthdayAlreadySetError,
    PhoneAlreadyExistsError,
    PhoneNotFoundError,
    UserNotFoundError,
    ValidationError,
)


def handle_error():
    def decorator(function: Callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)

            except ValidationError as e:
                return e.message
            except UserNotFoundError as e:
                return e.message
            except PhoneNotFoundError as e:
                return e.message
            except PhoneAlreadyExistsError as e:
                return e.message
            except BirthdayAlreadySetError as e:
                return e.message

            except ValueError or IndexError:
                return "Enter the argument for the command"

        return wrapper

    return decorator
