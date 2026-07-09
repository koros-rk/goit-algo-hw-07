class Field:
    def __init__(self, value):
        self.validate(value)
        self.value = value

    @classmethod
    def validate(cls, value):
        pass

    def __str__(self):
        return str(self.value)
