#!/usr/bin/python3
"""
   class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
       class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes Rectangle based on class BaseGeometry"""
        # super().integer_validator(width, height)
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Defines format in which print fn displays"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """Outputs human readable representation of class object"""
        return self.__str__()
