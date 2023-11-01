#!/usr/bin/python3
"""

"""


def matrix_mul(m_a, m_b):
    """"

    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if 
