#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


def max_integer(list=[]):
    if len(list) == 0:
        return None
    return max(list)
