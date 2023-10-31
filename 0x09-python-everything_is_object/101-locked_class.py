#!/usr/bin/python3
"""

"""


class LockedClass:
    """

    """
    __locked = False

    def __init__(self, first_name):
        self.__first_name = first_name

    def __setattr__(self, key, value):
        if self.__locked and not hasattr(self, key = first_name):
            raise AttributeError

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__firt_name = value

    def __freeze(self):
        self.__locked = True
