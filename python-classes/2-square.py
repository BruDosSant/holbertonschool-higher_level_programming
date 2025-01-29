#!/usr/bin/python3
"""

no se que poner es un cuadradinho

"""


class Square:
    """A simple example class"""
    def __init__(self, size=0):
        self._Square__size = size
    if not isinstance(_Square__size, int):
        raise TypeError ("size must be an integer")
    if _Square__size < 0:
        raise ValueError ("size must be >= 0")