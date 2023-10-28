#!/usr/bin/python3
"""
   Function that prints out a square with the symbol '#'
"""


def print_square(size):
    """
       Prints out a square with '#'
       Raises exception if size is not an int or
       is less than zero
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
