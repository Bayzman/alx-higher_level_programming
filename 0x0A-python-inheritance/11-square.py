#!/usr/bin/python3

""" Square class that inherits from the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from the Rectangle class
    """

    def __init__(self, size):
        """ Class instantiation """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Overwrites the print statement """
        return (f'[Square] {self._Square__size:d}/self._Square__size:d}')
