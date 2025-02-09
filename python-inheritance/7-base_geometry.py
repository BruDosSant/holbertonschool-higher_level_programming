#!/usr/bin/python3
"""
Clase BaseGeometry con los métodos area() y integer_validator().
"""


class BaseGeometry:
    """Clase base para geometría, con métodos para área y validación de enteros."""

    def area(self):
        """Lanza una excepción indicando que el área no está implementada."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida si value es un número entero mayor que 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
