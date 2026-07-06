from entitites.birthday import Birthday
from entitites.name import Name
from entitites.phone import Phone
from errors import PhoneAlreadyExistsError, PhoneNotFoundError


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def find_phone(self, phone: str):
        phones = [p for p in self.phones if str(p) == phone]
        return phones[0] if len(phones) > 0 else None

    def add_phone(self, phone):
        if not self.find_phone(phone):
            created = Phone(phone)
            return self.phones.append(created)
        raise PhoneAlreadyExistsError(phone)

    def edit_phone(self, old_phone: str, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def remove_phone(self, phone):
        user_phone = self.find_phone(phone)
        if user_phone:
            return self.phones.remove(user_phone)
        raise PhoneNotFoundError(phone)

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"[{self.birthday}] {self.name}: {', '.join(str(phone) for phone in self.phones)}"
