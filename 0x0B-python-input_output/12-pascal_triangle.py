#/!/usr/bin/python3

""" Returns a list of lists of integers representing the
    Pascal's triangle of n
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
         Pascal's triangle of n
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    triagle = []
    for i in range(n):
        row = [1]

        if i > 1:
            prev = triangle[i - 1]
            for j in range(1, i):
                val = prev[j - 1] + prev[j]
                row.append(val)

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
