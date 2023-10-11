#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
     squarefunc = lambda x : x * x
     newmatrix = [squarefunc(col) for row in matrix for col in row]
     return newmatrix
