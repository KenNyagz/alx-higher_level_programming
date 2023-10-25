#!/usr/bin/python3
""" Class square"""



class Square:
    """Coordinates of a square"""


    def __init__(self, size=0, position=(0, 0)):
    """
    Initailize a square

    Params:
        size (int): side of square
        position (tuple): locaation of square
    """
        self.__size = size

    @property
    def size(self):
    """Retrieve side of square"""
        return self.__size

    @size.setter
    def size(self, value):
    """

    """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
    """asad"""
        if self.__size == 0:

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
