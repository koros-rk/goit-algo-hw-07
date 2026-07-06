from decorators import handle_error, validate_payload
from entitites import AddressBook, Record
from errors import UserNotFoundError


@handle_error()
@validate_payload(schema={"name": str, "phone": str})
def add(*args, repository: AddressBook):
    name, phone = args

    try:
        user = repository.find(name)
        user.add_phone(phone)
        return f"Phone number {phone} for {name} has been added."
    except UserNotFoundError:
        user = Record(name)
        user.add_phone(phone)
        repository.add_record(user)
        return f"User ({user}) has been added."
