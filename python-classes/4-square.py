#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class Square:
    """A simple example class"""
    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        """Getter para obtener el tamaño del cuadrado."""
        return _Square__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        return self._Square__size * self._Square__size
