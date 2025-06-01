#!/usr/bin/python3
"""
9-rectangle.py
This module defines a Rectangle class that inherits from BaseGeometry.
It validates the width and height parameters and initializes them.
It is intended to be used as a base class for geometric shapes that require
width and height attributes.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase base para geometría con métodos para área y validación de int."""
    def __init__(self, width, height):
        """Lanza una excepción indicando que el área no está implementada."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación en string del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Devuelve una representación para recrear el objeto usando eval()"""
        return f"Rectangle({self.__width}, {self.__height})"
