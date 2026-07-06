from decorators import handle_error, validate_payload
from entitites import AddressBook


@handle_error()
@validate_payload(schema={"name": str})
def show_birthdays(*args, repository: AddressBook):
    (name,) = args

    user = repository.find(name)
    if not user.birthday:
        return f"{name} has no birthday set."
    return f"Birthday for {name} is {user.birthday}"
