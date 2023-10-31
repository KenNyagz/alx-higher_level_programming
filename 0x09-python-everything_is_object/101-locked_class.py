#!/usr/bin/python3
"""
   A locked class that oe cannot create attributes dynamically
"""


class LockedClass:
    """
       Only possible attribute is first_name instance attribute
    """
    __locked = False

    def __init__(self, first_name):
        self.__first_name = first_name

    def __setattr__(self, key, value):
        if self.__locked and key != 'first_name':
            raise AttributeError

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__firt_name = value

    def __freeze(self):
        self.__locked = True
