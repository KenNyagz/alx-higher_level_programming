#!/usr/bin/python3
""" Class square"""



class Square:
    """Coordinates of a square"""


    def __init__(self, size=0):
    """ sda"""
        self.__size = size

    @property
    def size(self):
    """dasd"""
        return self.__size

    @size.setter
    def size(self, value):
    """sasasd"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
    """asad"""
        if self.__size == 0:
