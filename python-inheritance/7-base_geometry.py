#!/usr/bin/python3
"""
7-base_geometry.py
This module defines a BaseGeometry class that serves as a base for
other geometric classes.
It includes methods for calculating the area and validating integer
values.
It raises exceptions for unimplemented methods and invalid values,
ensuring that subclasses
must provide their own implementations and adhere to specific constraints.
"""


class BaseGeometry:
    """Clase base para geometría con métodos para área y validación de int"""

    def area(self):
        """Lanza una excepción indicando que el área no está implementada."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida si value es un número entero mayor que 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
