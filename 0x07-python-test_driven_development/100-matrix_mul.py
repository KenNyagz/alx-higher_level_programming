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

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_b should contain only integers or floats")

    len_row_a = len(mat_a[0])
    for i in m_a:
        if len(i) != len_row_a:
            raise TypeError("each row of m_a must be of the same size")
    for j in m_b:
        if len(j) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")


