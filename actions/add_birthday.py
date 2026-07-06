from decorators import handle_error, validate_payload
from entitites import AddressBook


@handle_error()
@validate_payload(schema={"name": str, "birthday": str})
def add_birthday(*args, repository: AddressBook):
    name, birthday = args

    user = repository.find(name)
    user.add_birthday(birthday)
    return f"Birthday for {name} set to {user.birthday}."
