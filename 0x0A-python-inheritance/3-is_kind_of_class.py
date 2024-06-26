#!/usr/bin/python3

""" Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class,
    otherwise False
"""


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance of a class or a class
        that inherited from the specified class
    """

    return isinstance(obj, a_class)
