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

    def area(self) -> int:
        ''' Computes the area of a rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self) -> int:
        ''' Computes the perimeter of a rectangle
        '''
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        ''' prints rectangles using the # symbol
        '''
        symbol = ''
        if (self.__height == 0 or self.__width == 0):

            return symbol

        else:
            i = 0
            for i in range(self.__height):
                symbol += ('#' * self.__width)
                if (i != (self.__height - 1)):
                    symbol += '\n'

            return symbol
