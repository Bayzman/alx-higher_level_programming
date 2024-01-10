#!/usr/bin/python3
''' Returns True if the object is exactly an instance of the
    specified class, otherwise False
'''


def is_same_class(obj, a_class):
    ''' Check if an object is an instance of the specified class

    Args:
        obj (object): object
        a_class (object): object

    Return:
        True / False (bool)
    '''

    return type(obj) == a_class
