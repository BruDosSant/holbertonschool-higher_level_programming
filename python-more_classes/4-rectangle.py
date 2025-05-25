#!/usr/bin/python3
"""
0-rectangle.py
This module defines an empty class named `rectangle`.
It serves as a placeholder for future development.
"""


class Rectangle():
    """
    Doc de class, no hace nada
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """
        Prints the rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for i in range(self.__height):
                print("#" * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for i in range(self.__height):
            result += "#" * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result

        def __repr__(self):
        """
        Returns a string that can recreate the object with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
