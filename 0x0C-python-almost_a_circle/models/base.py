#!/usr/bin/python3
"""Ancestor class Base
"""


class Base:
    """Ancestor Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
