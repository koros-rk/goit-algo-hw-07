class UserNotFoundError(ValueError):
    def __init__(self, name: str):
        self.message = f"User {name} not found"

    def __str__(self):
        return self.message
