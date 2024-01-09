#!/usr/bin/python3
''' Get all attributes and methods of an object
'''


def lookup(obj):
    ''' Returns the list of available attributes and methods of
        an object

    Args:
         obj (object): object of a class

    Return:
         list: list of available attributes and mthods
    '''

    return dir(obj)
