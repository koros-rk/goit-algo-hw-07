from decorators import handle_error
from entitites import AddressBook


@handle_error()
def birthdays(*_, repository: AddressBook):
    upcoming = repository.get_upcoming_birthdays(31)
    lines = []

    for birthday in upcoming:
        lines.append(f"[{birthday.get('congratulation_date')}] {birthday.get('name')}")

    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(lines)
