#!/usr/bin/python3


""" Prints a square with the character # """


def print_square(size):
    """ Prints a square with the character # """

    msg = 'size must be an integer'

    if not isinstance(size, int):
        raise TypeError(msg)

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError(msg)

    for i in range(size):
        print('#' * size)
