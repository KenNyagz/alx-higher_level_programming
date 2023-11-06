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
        Calculates an area; raises an Exception
        """
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value to be sure it's int
        name is the name of the dimension whose value is given
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
