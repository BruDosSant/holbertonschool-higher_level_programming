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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        symbol = str(self.print_symbol)
        result = ""
        for i in range(self.__height):
            result += symbol * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """
        Returns a string that can recreate the object with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when the rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        print(f"Number of instances: {Rectangle.number_of_instances}")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the bigger area.
        If equal, returns rect_1.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.
        """
        return cls(size, size)
