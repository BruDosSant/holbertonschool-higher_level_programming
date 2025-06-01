#!/usr/bin/python3
"""
6-base_geometry.py
This module defines a BaseGeometry class that serves as a base for
other geometric classes.
It includes a method to calculate the area, which is expected to be
implemented by subclasses.
It raises an exception if the method is not implemented, enforcing that
subclasses must provide their own implementation.
"""


class BaseGeometry:
    """Clase que extiende list con un método para imprimir la lista ordenad"""
    def area(self):
        """Imprime la lista en orden ascendente sin modificar la original."""
        raise Exception("area() is not implemented")
