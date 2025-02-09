#!/usr/bin/python3
"""
Función que devuelve True si el objeto es una instancia exacta de la
clase especificada, de lo contrario, devuelve False.
"""


def is_kind_of_class(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    return isinstance(obj, a_class)
