#!/usr/bin/python3
"""
8-rectangle.py
This module defines a Rectangle class that inherits from BaseGeometry.
It validates the width and height parameters and initializes them.
The class is intended to represent a rectangle with specific dimensions.
It is useful for creating rectangle objects with validation of dimensions.
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
