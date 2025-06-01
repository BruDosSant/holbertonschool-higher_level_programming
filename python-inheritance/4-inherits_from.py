#!/usr/bin/python3
"""
Función que devuelve True si el objeto es una instancia exacta de la
clase especificada, de lo contrario, devuelve False.
"""


def inherits_from(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
