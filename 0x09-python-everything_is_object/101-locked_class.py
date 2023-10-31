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
        if hasattr(self, name) and name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Cannot create new instance attribute")
