#!/usr/bin/python3
"""
A class BaseGeometry
That validates only integers
Raises exception if not ints
"""


class BaseGeometry:
    """
    Class base geometry
    Check for integers, if not raises Exception
    """
    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".formart(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".formart(name))    
