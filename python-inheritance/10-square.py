#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle): 
    """Calcula el área del cuadrado."""
    def __init__(self, size):
        """Calcula el área del cuadrado."""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size
