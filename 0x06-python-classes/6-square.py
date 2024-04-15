#!/usr/bin/python3

""" Experimenting with classes
"""


class Square:
    """ Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Class initialization """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ Property decorator to get the size attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Property decorator to set the size attribute
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """ Decorator to get the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Decorator to set the position attribute
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(i, int) and i >= 0 for i in value):
        """ if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):"""
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Method to compute the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Print a square
        """
        if (self.__size == 0):
            print('')
        for i in range(self.__size):
            print('#' * self.__size)
