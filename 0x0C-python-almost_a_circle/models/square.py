#!/usr/bin/python3
"""class Square that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialiser"""
        super().__init__(size, size, x, y, id)
        
