#!/usr/bin/python3

''' Read a text file (UTF8)
'''


def read_file(filename='') -> None:
    ''' Reads a text file

    Args:
        filename (str): file name
    '''
    with open(filename) as f:
        for line in f:
           print(line, end='')
