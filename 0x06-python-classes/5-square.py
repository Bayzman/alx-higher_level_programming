#!/usr/bin/python3

''' Experimenting with classes
'''


class Square:
    ''' Square class
    '''

    def __init__(self, size=0):
        ''' Class initialization
        '''
        self.__size = size

    @property
    def size(self):
        ''' Property decorator to get the size attribute
        '''
        return self.__size

    @size.setter
    def size(self, size):
        ''' Property decorator to set the size attribute
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

    def my_print(self):
        ''' Print a square
        '''
        if (self.__size == 0):
            print('')
        for i in range(self.__size):
            print('#' * self.__size)
