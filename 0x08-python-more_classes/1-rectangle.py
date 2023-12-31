#!/usr/bin/python3
"""
   Create a class rectangle that has private height and width atrributes
   attributes must be ints
"""


class Rectangle:
    """
       Class that initiates rectangles.
    """
    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0
    # Use the width property setter to validate and set the width
        self.width = width
    # Use the height property setter to validate and set the height
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
