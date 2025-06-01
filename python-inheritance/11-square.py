#!/usr/bin/python3
"""
11-square.py
This module defines a Square class that inherits from Rectangle.
It implements the area method to calculate the area of the square.
It validates the size as a positive integer and provides string representations.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inheriting from Rectangle.
    Validates the size as a positive integer and implements the area method.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return the area of the square (size ** 2).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square
         in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Return a string representation of the square that allows
         recreation using eval().
        """
        return f"Square({self.__size})"
