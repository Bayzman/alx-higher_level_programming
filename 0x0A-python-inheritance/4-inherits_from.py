#!/usr/bin/python3
''' Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
'''


def inherits_from(obj, a_class):
    ''' Checks if an object is an instance of a class '''

    obj_type = type(obj)
    if (obj_type != a_class):
        return issubclass(obj_type, a_class)
    else:
        return False
