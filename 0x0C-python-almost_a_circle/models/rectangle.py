#!/usr/bin/python3
"""class Rectangle that inherits from Base
"""
from models.base import Base
# Base = __import__('base').Base


class Rectangle(Base):
    """Child to class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method"""
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter fn"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter fn"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ 'x' getter """
        return self.__x

    @x.setter
    def x(self, val):
        """ 'x' setter"""
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """ 'y' getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """ 'y' setter"""
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Return area of Rectangle class instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance
           with the character #
        """
        for i in range(self.y):
            print()

        for j in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """ printing format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute based on keywords"""
        if args:
            attr_list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
               }
