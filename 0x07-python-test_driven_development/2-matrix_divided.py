#!/usr/bin/python3

""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    msg1 = 'matrix must be a matrix (list of lists) of integers/floats'
    msg2 = 'Each row of the matrix must have the same size'
    msg3 = 'div must be a number'
    msg4 = 'division by zero'

    if not isinstance(matrix, list):
        raise TypeError(msg1)

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(msg1)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(msg2)

    if not isinstance(div, (int, float)):
        raise TypeError(msg3)

    if (div == 0):
        raise ZeroDivisionError('division by zero')

    matrix2 = []
    for row in matrix:
        result = list(map(lambda val: round(val/div, 2), row))
        matrix2.append(result)

    return matrix2
