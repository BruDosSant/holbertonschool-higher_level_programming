#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class BaseGeometry:
    """Clase que extiende list con un método para imprimir la lista ordenada"""
    def area(self):
        """Imprime la lista en orden ascendente sin modificar la original."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Imprime la lista en orden ascendente sin modificar la original."""
        if isinstance(value, int):
            raise ValueError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
