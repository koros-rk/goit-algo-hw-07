from entitites.field import Field
from errors import ValidationError


class Phone(Field):
    def __init__(self, value: str):

        if len(value) != 10 or not value.isnumeric():
            raise ValidationError("Invalid phone number format")
        super().__init__(value)
