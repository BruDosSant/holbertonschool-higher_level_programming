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
        self.set_size(size)

    def set_size(self, size):
        """
        Set the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def get_size(self):
        """
        Get the size
        """
        return self.__size
     def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2
