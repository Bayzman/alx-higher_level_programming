#!/usr/bin/python3

""" Multiplies 2 matrices by using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')

    if (len(m_a[0]) == 0):
        raise ValueError('m_a can\'t be empty')

    if (len(m_b[0]) == 0):
        raise ValueError('m_b can\'t be empty')

    for row in m_a:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError('m_b should contain only integers or floats')

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if (len(m_a[0]) != len(m_b)):
        raise ValueError('m_a and m_b can\'t be multiplied')

    m_a = np.array(m_a)
    m_b = np.array(m_b)
    result = np.dot(m_a, m_b)

    return result
