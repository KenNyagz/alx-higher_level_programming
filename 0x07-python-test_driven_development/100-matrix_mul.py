#!/usr/bin/python3
"""
   Function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
       Attempt to multiply to matrices; after verifying various checks
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_b should contain only integers or floats")

    len_rows_a = len(m_a[0])
    for i in m_a:
        if len(i) != len_rows_a:
            raise TypeError("each row of m_a must be of the same size")
    len_rows_b = len(m_b[0])
    for j in m_b:
        if len(j) != len_rows_b:
            raise TypeError("each row of m_b must be of the same size")

    # Check number of columns in 1st matrix is = to no of rows in the 2nd
    if len_rows_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    resMatrix = [[0 for el in range(len(m_b[0]))] for elm in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                resMatrix[i][j] += m_a[i][k] * m_b[k][j]

    return resMatrix
