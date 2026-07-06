from decorators import handle_error, validate_payload
from entitites import AddressBook


@handle_error()
@validate_payload(schema={"name": str})
def show_phones(*args, repository: AddressBook):
    (name,) = args
    user = repository.find(name)
    return ", ".join([phone.value for phone in user.phones])
