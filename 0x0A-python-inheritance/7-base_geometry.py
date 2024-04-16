#!/usr/bin/python3

""" Create an Base Geometry class """


class BaseGeometry:
    """ Base Geometry """

    def area(self) -> Exception:
        """ Raise an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value) -> Exception:
        """ Integer validator """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')

        if (value <= 0):
            raise ValueError(f'{name} must be greater than 0')
