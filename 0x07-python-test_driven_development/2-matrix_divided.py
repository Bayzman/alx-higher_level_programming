#!/usr/bin/python3
''' Divides all elements of a matrix '''

def matrix_divided(matrix, div):
    ''' Divides all elements of a matrix '''
    msg = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(msg)

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(msg)

    # Check for size of rows
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if (div == 0):
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda val: round(val/div, 2), row)))

    return new_matrix
