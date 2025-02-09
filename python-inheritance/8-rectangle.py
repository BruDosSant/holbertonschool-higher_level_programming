#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Clase que extiende list con un método para imprimir la lista ordenada"""
    def __init__(self, width, height):
        # Validar los valores de width y height usando integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height