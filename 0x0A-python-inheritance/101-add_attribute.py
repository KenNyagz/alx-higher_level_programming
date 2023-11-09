#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object if it’s possible"""
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
