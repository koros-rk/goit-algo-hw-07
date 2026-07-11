from collections import UserDict
from datetime import datetime, timedelta

from entitites.record import Record
from errors import UserNotFoundError


class AddressBook(UserDict[str, Record]):
    def find(self, name: str):
        user = self.data.get(name.casefold())
        if user:
            return user
        raise UserNotFoundError(name)

    def add_record(self, record: Record):
        key = record.name.value.casefold()
        self.data.update({key: record})

    def delete_record(self, name: str):
        if name.casefold() in self.data:
            del self.data[name.casefold()]
            return
        raise UserNotFoundError(name)

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays: list[dict] = []
        today = datetime.today()

        for key, user in self.data.items():
            if not user.birthday:
                continue

            birthday = datetime.strptime(user.birthday.value, "%d.%m.%Y")
            birthday = birthday.replace(year=today.year)

            if 0 <= (birthday - today).days <= days:
                adjusted_birthday = self.__adjust_for_weekend(birthday)
                congratulation_date_str = self.__date_to_string(adjusted_birthday)
                upcoming_birthdays.append(
                    {
                        "name": user.name.value,
                        "congratulation_date": congratulation_date_str,
                    }
                )

        return upcoming_birthdays

    @classmethod
    def __prepare_user_list(cls, user_data):
        prepared_list = []
        for user in user_data:
            prepared_list.append(
                {
                    "name": user["name"],
                    "birthday": cls.__string_to_date(
                        user["birthday"],
                    ),
                }
            )
        return prepared_list

    @classmethod
    def __adjust_for_weekend(cls, birthday: datetime):
        if birthday.weekday() >= 5:
            return cls.__find_next_weekday(birthday, 0)
        return birthday

    @staticmethod
    def __string_to_date(date_string: str):
        return datetime.strptime(date_string, "%Y.%m.%d").date()

    @staticmethod
    def __date_to_string(date):
        return date.strftime("%Y.%m.%d")

    @staticmethod
    def __find_next_weekday(start_date: datetime, weekday: int):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
