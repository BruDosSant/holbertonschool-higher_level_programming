#!/usr/bin/python3
"""
3-is_kind_of_class.py
This module provides a function to check if an object is an instance of a 
specified class or its subclasses.
It is useful for type checking and ensuring that an object conforms to a 
specific class hierarchy.
"""


def is_kind_of_class(obj, a_class):
    """Verifica si obj es exactamente una instancia de a_class."""
    return isinstance(obj, a_class)
