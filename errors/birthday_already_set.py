class BirthdayAlreadySetError(ValueError):
    def __init__(self, user: str):
        self.message = f"Birthday already set for {user}."

    def __str__(self):
        return self.message
