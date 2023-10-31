#!/usr/bin/python3
"""
   A locked class that oe cannot create attributes dynamically
"""


class LockedClass:
    """
       Only possible attribute is first_name instance attribute
    """
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if name != 'first_name':
             raise AttributeError
        super().__setattr__(name, value)
