#!/usr/bin/python3
"""
0-lookup.py
This module provides a function to retrieve the list of attributes and methods
of an object.
It is useful for introspection and understanding the capabilities of objects
 in Python.
"""


def lookup(obj):
    """ Returns a list of available attributes and methods of an object"""
    messi = dir(obj)
    return messi
