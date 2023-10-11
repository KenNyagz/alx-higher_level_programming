#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
     squarefunc = lambda x : x * x
     newmatrix = [[squarefunc(col) for col in row] for row in matrix]
     return newmatrix
