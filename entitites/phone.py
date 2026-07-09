from entitites.field import Field
from errors import ValidationError


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def validate(cls, value: str):
        if len(value) != 10 or not value.isnumeric():
            raise ValidationError("Invalid phone number format")
