#!/usr/bin/python3

""" Adds attributes to an object """


def add_attribute(obj, attr, val):
    """ Adds attr to an object """

    out = getattr(obj, '__dict__', None)
    if out == {}:
        setattr(obj, attr, val)
    else:
        raise TypeError('can\'t add new attribute')
