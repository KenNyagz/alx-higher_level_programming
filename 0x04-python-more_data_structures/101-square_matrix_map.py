#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    cp_matrix = []
    for row in matrix:
        cp_row = []
        for elm in row:
            cp_elm = elm ** 2 
            cp_row.append(cp_elm)
        cp_matrix.append(cp_row)

    return cp_matrix
