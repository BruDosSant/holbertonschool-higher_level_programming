#!/usr/bin/python3
"""Este es un módulo que contiene una función para sumar d"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print('#' * size)
