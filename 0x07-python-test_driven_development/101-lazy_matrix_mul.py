#!/usr/bin/python3

""" Multiplies 2 matrices by using the module NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices """
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    result = np.dot(m_a, m_b)
    return result
