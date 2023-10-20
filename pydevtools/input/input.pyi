def get_input(prompt: str, color: str) -> str:
    """
    Get user input with a colorized prompt using Colorama.

    Args:
        prompt (str): The prompt message to display.
        color (str): The color for the prompt. Should be one of the Colorama color constants.

    Returns:
        str: The user's input as a string.
    """

def get_strinput(prompt: str, color: str) -> str:
    """
    Get user input with a colorized prompt using Colorama and expect a string input.

    Args:
        prompt (str): The prompt message to display.
        color (str): The color for the prompt. Should be one of the Colorama color constants.

    Returns:
        str: The user's input as a string.
    """

def get_intinput(prompt: str, color: str) -> int:
    """
    Get user input with a colorized prompt using Colorama and expect an integer input.

    Args:
        prompt (str): The prompt message to display.
        color (str): The color for the prompt. Should be one of the Colorama color constants.

    Returns:
        int: The user's input as an integer.

    Raises:
        ValueError: If the user input cannot be converted to an integer.
    """

def get_floatinput(prompt: str, color: str) -> float:
    """
    Get user input with a colorized prompt using Colorama and expect a float input.

    Args:
        prompt (str): The prompt message to display.
        color (str): The color for the prompt. Should be one of the Colorama color constants.

    Returns:
        float: The user's input as a float.

    Raises:
        ValueError: If the user input cannot be converted to a float.
    """
