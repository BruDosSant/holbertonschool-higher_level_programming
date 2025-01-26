#!/usr/bin/python3
"""
Module that adds two integers.

This module defines a function that adds two integers, handling cases where
the inputs are floats or non-integer types. If a non-integer or float is provided,
it raises a TypeError with the corresponding message.

Function:
    add_integer(a, b=98): Adds two integers or floats and returns the sum as an integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of the two arguments, casted to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
