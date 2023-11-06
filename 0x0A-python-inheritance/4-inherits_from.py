#!/usr/bin/python3
"""
   function that returns True if the object is an instance of a class that in-
   herited (directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
       Checks if an object is of a subclass of the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
