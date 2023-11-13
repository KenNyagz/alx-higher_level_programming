#!/usr/bin/python3
"""class Square that inherits from Rectangle
"""
from .rectangle import Rectangle
# Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialiser"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print format"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
               }
