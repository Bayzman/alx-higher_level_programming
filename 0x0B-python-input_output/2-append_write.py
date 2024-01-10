#!/usr/bin/python3
''' Append a string at the end of a text file
'''


def append_write(filename='', text='') -> int:
    ''' Append a string at the end of a text file

    Args:
        filename (str): file name
        text (str): string to append

    Return:
        number of a characters added (int)
    '''
    with open(filename, 'a') as f:
        f.write(text)

    return len(text)
