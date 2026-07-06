from colorama import Fore


def default(command: str):
    return f"Command {Fore.GREEN}{command}{Fore.RESET} not found."
