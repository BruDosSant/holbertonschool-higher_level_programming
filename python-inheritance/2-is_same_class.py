#!/usr/bin/python3
"""
Función que devuelve True si el objeto es una instancia exacta de la clase,
de lo contrario, devuelve False.
"""


def is_same_class(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    return type(obj) == a_class
