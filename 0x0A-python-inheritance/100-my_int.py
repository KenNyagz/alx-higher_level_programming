#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """ inherits from 'int'"""
    def __eq__(self, other):
        """the == comparison inversion"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ the != comparison operator"""
        return super().__eq__(other)
