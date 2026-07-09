from entitites.field import Field
from errors import ValidationError


class Name(Field):
    def __init__(self, value):
        super().__init__(value.title())

    @classmethod
    def validate(cls, value):
        if len(value) == 0:
            raise ValidationError("Name cannot be empty")
