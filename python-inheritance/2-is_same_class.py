#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    return isinstance(obj, a_class) and type(obj) is a_class
