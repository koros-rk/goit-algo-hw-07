class UserAlreadyExistsError(Exception):
    def __init__(self, phone: str):
        self.message = f"User {phone} already exists"

    def __str__(self):
        return self.message
