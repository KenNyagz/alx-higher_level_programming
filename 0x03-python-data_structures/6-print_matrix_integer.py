#!/usr/bin/python3
def element_lengths(matrix=[[]]):
    return [len(str(element)) for row in matrix for element in row]

def alt_max(seq):
    mx = seq[0]
    for item in seq:
        if item > mx:
            mx = item
    return mx

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    lengths = element_lengths(matrix)
    max_width = alt_max(lengths)

    for row in matrix:
        for elem in row:
            print("{:>{}}".format(elem, max_width), end=' ')
        print()
