#!/usr/bin/python3

def add_integer(a, b=98):
        """
        Sums two integers or floats and returns the result as an integer.

        Parameters:
        a (int, float): The first number to be added.
        b (int, float, optional): The second number to be added. Default is 98.

        Returns:
        int: The sum of a and b, after converting both to integers.

        Raises:
        TypeError: If either a or b are not integers or floats.
        """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    
    return a + b
