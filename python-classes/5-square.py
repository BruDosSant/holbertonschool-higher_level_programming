#!/usr/bin/python3
"""
1-square.py
"""


class Square:
    """
    Class Square that defines a square by its size.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa el atributo size utilizando el setter.
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        Print the square with the character #.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

    @property
    def position(self):
        """
        Get the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
