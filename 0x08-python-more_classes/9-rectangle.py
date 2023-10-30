#!/usr/bin/python3
"""
   A Class Rectangle that takes two integers and intanciates a rectangle
   Only takes positive integers lest raises an error
   has method that returns a printable string representation of obj using "#"
   has method that return a str representation of an instance
   contains method that delete objects
   Class variable adjust
"""


class Rectangle:
    """
       Class Rectangle that intantiates a rectangle
       __str__ method gets a printable string representation of obj using "#"
       __repr__ method returns human readable object representation
       __del__ instance method that deletes an obj when del is called
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # self.__width = 0
        # self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rect_str += str(self.print_symbol) * self.__width
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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares areas of two rectangles and returns the bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Instantiates new Rectangle object with all sides equal"""
        sqr = Rectangle(size, size)
        return sqr
