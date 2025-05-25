#!/usr/bin/python3
"""
1-square.py
"""


class Square:
    """
    Class Square that defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Inicializa el atributo size utilizando el setter.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2
