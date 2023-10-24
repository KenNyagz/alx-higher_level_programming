#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square with hidden attribute"""

    def __init__(self, size=0):
        try:
            if not int(size):
                raise TypeError
        except TypeError:
                print("size must be an integer")
        try:
            if size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
        finally:
            self.__size = size
