#!/usr/bin/python3
"""
4-inherits_from.py
This module provides a function to check if an object is an instance of a 
specified class,
or a subclass of that class, but not an instance of the class itself.
It is useful for determining inheritance relationships in Python's
object-oriented programming.
"""


def inherits_from(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
