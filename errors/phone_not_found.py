class PhoneNotFoundError(Exception):
    def __init__(self, phone: str):
        self.message = f"Phone {phone} not found"

    def __str__(self):
        return self.message
