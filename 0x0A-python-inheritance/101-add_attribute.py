#!/usr/bin/python3
"""

"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object
    """
    if '__dict__' in dir(obj):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
