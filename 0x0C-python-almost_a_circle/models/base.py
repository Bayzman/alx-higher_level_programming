#!/usr/bin/python3
''' First class Base '''


class Base:
    ''' first class Base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Instantiate class (class constructor) '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
