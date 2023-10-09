#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for row in matrix:
        for elem in row:
            print("{: >2}".format(elem), end=' ')
        print()
