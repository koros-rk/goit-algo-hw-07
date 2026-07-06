from actions import (
    add,
    add_birthday,
    all,
    birthdays,
    change_phone,
    default,
    hello,
    show_birthdays,
    show_phones,
)
from entitites import AddressBook, Record

HANDLERS = {
    "all": all,
    "hello": hello,
    "add": add,
    "change": change_phone,
    "phone": show_phones,
    "add-birthday": add_birthday,
    "show-birthday": show_birthdays,
    "birthdays": birthdays,
}


def main():
    repository = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        args_array = input("Enter a command: ").split()

        if len(args_array) < 1:
            print("Invalid argument provided.")
            continue

        command, *args = args_array
        command_handler = HANDLERS.get(command.casefold())

        if command in ["exit", "quit"]:
            print("Goodbye!")
            break

        if command_handler:
            print(command_handler(*args, repository=repository))
        else:
            print(default(command))


if __name__ == "__main__":
    main()
