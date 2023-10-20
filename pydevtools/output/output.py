from colorama import Fore, Style


def print_output(message, color="white"):
    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    selected_color = color_map.get(color, Fore.WHITE)
    reset_style = Style.RESET_ALL

    print(f"{selected_color}{message}{reset_style}")


def print_info(message):
    print(f"{Fore.GREEN}[INFO]: {message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}[WARNING]: {message}{Style.RESET_ALL}")


def print_error(message):
    print(f"{Fore.RED}[ERROR]: {message}{Style.RESET_ALL}")
