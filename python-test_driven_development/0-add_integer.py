#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns the sum of two integers, a and b. 
    If a or b are floats, they are casted to integers.
    Raises a TypeError if a or b are not integers or floats."""
    # Check if 'a' is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if 'b' is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Cast 'a' and 'b' to integers if they are floats
    a = int(a)
    b = int(b)
    # Return the sum of a and b as an integer
    return a + b
