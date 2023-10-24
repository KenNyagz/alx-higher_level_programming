#!/usr/bin/python3
"""Area of a square"""


class Square:
    """ Publi instance"""
    
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        def area(self, size):
            return size ** 2
