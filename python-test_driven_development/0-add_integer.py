#!/usr/bin/python3
"""Este es un módulo que contiene una función para sumar d"""


def add_integer(a, b=98):
    """Suma dos números enteros y devuelve el resultado"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
