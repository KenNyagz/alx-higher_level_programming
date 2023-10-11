#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newmatrix = [[(col * col) for col in row] for row in matrix]
    return newmatrix
