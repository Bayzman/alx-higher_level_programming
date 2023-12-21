#!/usr/bin/python3

''' Experimenting with classes
'''


class Square:
    ''' Square class
    '''

    def __init__(self, size=0):
        ''' Class initialization
        Args:
             size (int, optional)
        Raises:
               TypeError: size must be an integer
               ValueError: size must be >= 0
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
