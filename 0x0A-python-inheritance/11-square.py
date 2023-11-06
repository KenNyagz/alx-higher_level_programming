#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    private instance attributes
    no getters or setters
    """
    def __init__(self, size):
        """Initialises a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcs the area of square"""
        return self.__size ** 2

    def __str__(self):
        """Provide a string with specific display format"""
        return "[Square] {}/{}".format(self.__size, self.__size)
