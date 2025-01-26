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
    Adds two integers or floats. If a float is provided, it will be cast to an integer before addition.
    If the inputs are not integers or floats, a TypeError will be raised.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).
    
    Returns:
        int: The sum of the two numbers as an integer.
    
    Raises:
        TypeError: If either a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast the float values to integers before adding them
    a = int(a)
    b = int(b)
    
    return a + b
