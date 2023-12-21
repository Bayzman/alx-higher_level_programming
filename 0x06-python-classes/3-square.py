#!/usr/bin/python3

''' Experimenting with classes
'''


class Square:
    ''' Square class
    '''

    def __init__(self, size=0):
        ''' Class initialization
        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' Method to compute the area of a square
        '''

        return self.__size * self.__size
