#!/usr/bin/python3
"""
   Function that divides each element of a matrix by a given number
   and returns a new matrix with the elements subject to the division
"""


def matrix_divided(matrix, div):
    """
       Divides all elements of a matrix by a number
       provided all the elements are either ints or doubles
    """

    if div is None:
        raise TypeError("div must be a number")

    # check matrix arg is valid matrix
    if not isinstance(matrix, list) or\
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
           "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    rowsize = len(matrix[0])
    for row in matrix:
        if len(row) != rowsize:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
            else:
                column = round((column / div), 2)
                new_row.append(column)
        new_matrix.append(new_row)

    return new_matrix

# print(matrix_divided(None, -2))
