#!/usr/bin/python3
''' Write a string to a file '''


def write_file(filename='', text='') -> int:
    ''' Write a string to a file

    Args:
        filename (str): file name
        text (str): string to write

    Return:
        number of characters written (int)
    '''
    with open(filename, 'w') as f:
        f.write(text)

    return len(text)
