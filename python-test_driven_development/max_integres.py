#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


def max_integer(lst=[]):
    """return max
        If the list is empty, the function returns None
    """
    
    if len(lst) == 0:
        return None
    
    maxi = lst[0]
    for i in lst[1:]:
        if i > maxi:
            maxi = i
    
    return maxi