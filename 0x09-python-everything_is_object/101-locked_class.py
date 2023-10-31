#!/usr/bin/python3
"""
   A locked class that oe cannot create attributes dynamically
"""


class LockedClass:
    """
       Only possible attribute is first_name instance attribute
    """

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError("'LockedClass' object\
                                 has no attribute '{}'".format(name))
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name != "first_name":
            raise AttributeError("'LockedClass' object\
                                 has no attribute'{}'".format(name))
        supe().__delattr__(name)
