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

Example:
    To add numbers: result = add(2, 3, 5)
    To subtract numbers: result = sub(10, 2, 3)
    To multiply numbers: result = mult(2, 3, 4)
    To divide numbers: result = div(20, 2, 5)
"""


def add(*nums: int | float) -> int | float:
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
    total = 0
    for num in nums:
        total = total + num
    return total


def sub(*nums: int | float) -> int | float:
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
    if len(nums) != 0:
        total = nums[0]
        for num in nums[1:]:
            total = total - num
        return total
    return 0


def mult(*nums: int | float) -> int | float:
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
    total = 1
    for num in nums:
        total = total * num
    return total


def div(*nums: int | float) -> int | float:
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
    if len(nums) != 0:
        total = nums[0] * nums[0]
        for num in nums:
            total = total / num
        return total
    return 1

def rem(a: int | float, b: int | float) -> int | float:
    """
    module of two numbers.

    Args:
        a (int or float): number.
        b (int or float): number.

    Returns:
        int or float: The result of modulo operation.

    Example:
        >>> rem(70, 35)
        0
    """
    return a % b
