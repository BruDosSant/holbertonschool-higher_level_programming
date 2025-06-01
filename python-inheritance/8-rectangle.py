#!/usr/bin/python3
"""

no se que poner es un cuadradinho

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
