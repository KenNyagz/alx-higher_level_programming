#!/usr/bin/python3
"""A class rectangle that inherits from BaseGeometry"""
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
