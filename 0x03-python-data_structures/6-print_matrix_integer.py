#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    max_width = max(len(str(element)) for row in matrix for element in row)
    for row in matrix:
        for elem in row:
            print("{:>{}}".format(elem, max_width), end=' ')
        print()
