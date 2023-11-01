#!/usr/bin/python3
"""
   add_integer - a function that adds two integers and returns teh result
   if a either a or b is a float they are first converted to integers
   If there is a none integer it raises an error(TypeError)
"""


def add_integer(a, b=98):
    """
       Adds two integers and returns the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf'):
        raise ValueError("a cannot be positive infinity")

    a = int(a)
    b = int(b)
    return a + b
