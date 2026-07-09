import datetime
import re

from entitites.field import Field
from errors import ValidationError


class Birthday(Field):
    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def validate(cls, value: str):
        pattern = re.compile(r"^(\d{2}).(\d{2}).(\d{4})$")
        if pattern.fullmatch(value) is None:
            raise ValidationError("Invalid date format")
        try:
            datetime.datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValidationError("Invalid date format")
