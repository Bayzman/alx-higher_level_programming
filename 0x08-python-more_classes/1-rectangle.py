#!/usr/bin/python3

''' Rectangle class
'''


class Rectangle:
    ''' Rectangle class

    Attributes:
        height (int)
        width (int)
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        ''' getter for width

        Returns:
            int: width
        '''
        return self.__width

    @width.setter
    def width(self, width) -> None:
        ''' setter for width
        '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self) -> int:
        ''' getter for height
        '''
        return self.__height

    @height.setter
    def height(self, height) -> None:
        ''' setter for height
        '''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
