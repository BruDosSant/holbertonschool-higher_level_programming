#!/usr/bin/python3

"""
Class Square inherits from Rectangle.

Usage:
    You can create instances of Square and it will validate size.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inheriting from Rectangle.
    
    Validates the size as a positive integer and implements the area method.
    """

    def __init__(self, size):
        self.integer_validator("size", size)  # Llamar a la validación de Rectangle
        self.__size = size  # Tamaño privado
        super().__init__(size, size)  # Llamar al constructor de Rectangle con el mismo tamaño para width y height

    def area(self):
        """
        Return the area of the square (size ** 2).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """
        Return a string representation of the square that allows recreation using eval().
        """
        return f"Square({self.__size})"
