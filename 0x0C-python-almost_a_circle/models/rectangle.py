#!/usr/bin/python3
"""class Rectangle that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """Child to class Base
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method"""
        super().__init__(id)
        self.__width = height
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter fn"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter fn"""
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.__height = height

    @property
    def x(self):
        """ 'x' getter """
        return self.__x

    @x.setter
    def x(self, val):
        """ 'x' setter"""
        self.__x = val

    @property
    def y(self):
        """ 'y' getter"""
        return self.__y

    @y.setter
    def y(self, val):
        """ 'y' setter"""
        self.__y = val
