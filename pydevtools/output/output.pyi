def print_output(message, color="white") -> None:
    """
    Print a message with optional colorization using Colorama.

    Args:
        message (str): The message to be displayed.
        color (str, optional): The color for the message. Should be one of the Colorama color constants.
            Defaults to "white" if not specified.

    Returns:
        None
    
    Example:
        >>> print_output("Success!", "green")
        "Success!"
    """

def print_info(message: str) -> None:
    """
    Print an informational message in green color.

    Args:
        message (str): The informational message to print.

    Returns:
        None

    Example:
        >>> print_info("This is an informational message.")
        [INFO]: This is an informational message.
    """

def print_warning(message: str) -> None:
    """
    Print a warning message in yellow color.

    Args:
        message (str): The warning message to print.

    Returns:
        None

    Example:
        >>> print_warning("This is a warning message.")
        [WARNING]: This is a warning message.
    """

def print_error(message: str) -> None:
    """
    Print an error message in red color.

    Args:
        message (str): The error message to print.

    Returns:
        None

    Example:
        >>> print_error("This is an error message.")
        [ERROR]: This is an error message.
    """
