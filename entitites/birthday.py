import re
from datetime import datetime

from entitites.field import Field
from errors import ValidationError


class Birthday(Field):
    def __init__(self, value: str):
        pattern = re.compile(r"^(\d{2}).(\d{2}).(\d{4})$")

        if pattern.fullmatch(value) is None:
            raise ValidationError("Invalid date format")

        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise ValidationError("Invalid date provided")
