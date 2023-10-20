from colorama import Fore, Style

def get_input(prompt, color):
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

    user_input = input(f"{selected_color}{prompt}: {Style.RESET_ALL}")

    return user_input

def get_strinput(prompt, color):
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

    user_input = input(f"{selected_color}{prompt} (str): {Style.RESET_ALL}")

    return user_input

def get_intinput(prompt, color):
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

    user_input = input(f"{selected_color}{prompt} (int): {Style.RESET_ALL}")

    try:
        int_input = int(user_input)
        return int_input
    except ValueError:
        raise ValueError("Input must be an integer.")

def get_floatinput(prompt, color):
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

    user_input = input(f"{selected_color}{prompt} (float): {Style.RESET_ALL}")

    try:
        float_input = float(user_input)
        return float_input
    except ValueError:
        raise ValueError("Input must be a float.")
