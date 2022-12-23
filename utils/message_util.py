from colorama import Fore

def error_message(message: str = "") -> None:
    print(f'{Fore.RED} Error: {message}')
