#!/usr/bin/python3
"""
   A Class Rectangle that takes two integers and intanciates a rectangle
   Only takes positive integers lest raises an error
   has method that returns a printable string representation of obj using "#"
   has method that return a str representation of an instance
   contains method that delete objects
"""


class Rectangle:
    """
       Class Rectangle that intanciates a rectangle
       __str__ method gets a printable string representation of obj using "#"
       __repr__ method returns human readable object representation
       __del__ instance method that deletes an obj when del is called
    """
    def __init__(self, width=0, height=0):
        # self.__width = 0
        # self.__height = 0
        self.width = width
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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.__height):
                rect_str += "#" * self.__width
                if i != self.__height - 1:
                    rect_str += "\n"
            return rect_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
           Prints when deleting instance
        """
        print("Bye rectangle...")
