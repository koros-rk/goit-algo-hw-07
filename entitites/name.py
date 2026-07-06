from entitites.field import Field
from errors import ValidationError


class Name(Field):
    def __init__(self, value):
        if len(value) == 0:
            raise ValidationError("Name cannot be empty")
        self.value = value.title()
        super().__init__(value)
