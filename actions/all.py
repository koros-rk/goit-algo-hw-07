from decorators import handle_error
from entitites import AddressBook


@handle_error()
def all(*_, repository: AddressBook):
    if not repository:
        return "No persons found."

    return str(repository)
