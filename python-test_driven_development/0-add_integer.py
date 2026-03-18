#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
It contains one function: add_integer(a, b=98).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    Args:
        a: The first number (must be an integer or float).
        b: The second number (must be an integer or float, defaults to 98).

    Returns:
        An integer representing the addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
