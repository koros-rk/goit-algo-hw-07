from decorators import handle_error, validate_payload
from entitites import AddressBook


@handle_error()
@validate_payload(schema={"name": str, "old_phone": str, "new_phone": str})
def change_phone(*args, repository: AddressBook):
    name, old_phone, new_phone = args

    user = repository.find(name)
    user.edit_phone(old_phone, new_phone)
    return f"Phone number for {name} changed from {old_phone} to {new_phone}."
