#!/usr/bin/python3
"""
   A locked class that oe cannot create attributes dynamically
"""


class LockedClass:
    """
       Only possible attribute is first_name instance attribute
    """
    __slots__ = ('first_name',)

    def __setattr__(self, key, value):
        if hasattr(self, name):
             super().__setattr__(name, value)
        elif name == 'first_name':
             super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute {name}'")

    #@property
    #def first_name(self):
     #   return self.__first_name

    #@first_name.setter
    #def first_name(self, value):
     #   self.__firt_name = value

    #def __freeze(self):
        #self.__locked = True'
