#!/usr/bin/python3
"""
   function that returns the list of available attributes
   and methods of an object
"""

def lookup(obj):
    """
       gets object's list of available attributes nad methods
    """
    return list(dir(obj))
