#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats.
    a and b must be integers or floats. If either is a float, it will be cast to an integer.
    Raises a TypeError if a or b are not integers or floats.
    Args:
        a (int, float): The first number.
        b (int, float): The second number (default is 98).
    Returns:
        int: The sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
