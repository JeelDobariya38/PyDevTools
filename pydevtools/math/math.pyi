"""
math.py - Mathematical Operations Module

This module provides basic mathematical operations such as addition,
subtraction, multiplication, and division on numbers. It is designed
to be flexible with support for variable-length argument lists.

Functions:
- add(*nums: int | float) -> int | float: Adds multiple numbers.
- sub(*nums: int | float) -> int | float: Subtracts numbers.
- mult(*nums: int | float) -> int | float: Multiplies numbers.
- div(*nums: int | float) -> int | float: Divides numbers.
"""

from typing import Union

def add(*nums: Union[int, float]) -> Union[int, float]:
    """
    Adds multiple numbers.

    Args:
        *nums (int or float): Variable-length list of numbers to be added.

    Returns:
        int or float: The sum of the provided numbers.

    Example:
        >>> add(2, 3, 5)
        10
    """

def sub(*nums: Union[int, float]) -> Union[int, float]:
    """
    Subtracts numbers.

    Args:
        *nums (int or float): Variable-length list of numbers.
            Subtracts each subsequent number from the first.

    Returns:
        int or float: The result of subtraction.

    Example:
        >>> sub(10, 2, 3)
        5
    """

def mult(*nums: Union[int, float]) -> Union[int, float]:
    """
    Multiplies numbers.

    Args:
        *nums (int or float): Variable-length list of numbers to be multiplied.

    Returns:
        int or float: The product of the provided numbers.

    Example:
        >>> mult(2, 3, 4)
        24
    """

def div(*nums: Union[int, float]) -> Union[int, float]:
    """
    Divides numbers.

    Args:
        *nums (int or float): Variable-length list of numbers.
            Divides each subsequent number by the first.

    Returns:
        int or float: The result of division.

    Example:
        >>> div(20, 2, 5)
        2.0
    """

def rem(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Module of two numbers.

    Args:
        a (int or float): Number.
        b (int or float): Number.

    Returns:
        int or float: The result of modulo operation.

    Example:
        >>> rem(70, 35)
        0
    """
