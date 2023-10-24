#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square with hidden attribute"""

    def __init__(self, size=0):
        if not int(size):
            try:
                raise TypeError
            except TypeError:
                print("size must be an integer")
        elif size < 0:
            try:
                raise ValueError
            except ValueError:
                print("size must be >= 0")
        else:
            self.__size = size
