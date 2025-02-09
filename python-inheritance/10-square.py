#!/usr/bin/python3

"""
retun true if is of that class

Usage:
You can create instances of Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    retun true if is of that class

    Usage:
    You can create instances of Rectangle.
    """
    def __init__(self, size):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size <= 0:
            raise ValueError("size must be greater than 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
