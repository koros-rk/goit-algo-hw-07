class PhoneAlreadyExistsError(Exception):
    def __init__(self, phone: str):
        self.message = f"Phone {phone} already exists"

    def __str__(self):
        return self.message
