#!/usr/bin/python3
"""
a function def pascal_triangle(n): that returns a list of lists of integers
 representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n < 0:
        return []
