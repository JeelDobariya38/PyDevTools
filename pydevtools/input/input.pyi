from colorama import Fore, Style

def get_input(prompt: str, color: str = "white") -> str:
    """
    Get user input with an optional colorized prompt using Colorama.

    Args:
        prompt (str): The prompt message to display.
        color (str, optional): The color for the prompt. Should be one of the Colorama color constants.
            Defaults to "white" if not specified.

    Returns:
        str: The user's input as a string.
    """

def get_strinput(prompt: str, color: str = "white") -> str:
    """
    Get user input with an optional colorized prompt using Colorama and expect a string input.

    Args:
        prompt (str): The prompt message to display.
        color (str, optional): The color for the prompt. Should be one of the Colorama color constants.
            Defaults to "white" if not specified.

    Returns:
        str: The user's input as a string.
    """

def get_intinput(prompt: str, color: str = "white") -> int:
    """
    Get user input with an optional colorized prompt using Colorama and expect an integer input.

    Args:
        prompt (str): The prompt message to display.
        color (str, optional): The color for the prompt. Should be one of the Colorama color constants.
            Defaults to "white" if not specified.

    Returns:
        int: The user's input as an integer.

    Raises:
        ValueError: If the user input cannot be converted to an integer.
    """

def get_floatinput(prompt: str, color: str = "white") -> float:
    """
    Get user input with an optional colorized prompt using Colorama and expect a float input.

    Args:
        prompt (str): The prompt message to display.
        color (str, optional): The color for the prompt. Should be one of the Colorama color constants.
            Defaults to "white" if not specified.

    Returns:
        float: The user's input as a float.

    Raises:
        ValueError: If the user input cannot be converted to a float.
    """
