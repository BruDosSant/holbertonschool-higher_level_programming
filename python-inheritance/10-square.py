#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Devuelve la representación en string del rectángulo."""
    def __init__(self, size):
        """Devuelve la representación en string del rectángulo."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Devuelve la representación en string del rectángulo."""
        return self.__size ** 2
