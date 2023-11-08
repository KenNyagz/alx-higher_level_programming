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
    if n <= 0:
        return []

    pasctri = [[0]*n for col in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                pasctri[i][j] = 1
            else:
                pasctri[i][j] = pasctri[i-1][j-1] + pasctri[i-1][j]
    return pasctri
