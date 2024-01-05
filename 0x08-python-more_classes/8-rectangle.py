#!/usr/bin/python3

''' Rectangle class
'''


class Rectangle:
    ''' Rectangle class

    Attributes:
        height (int)
        width (int)
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                symbol += (str(self.print_symbol) * self.__width)
                if (i != (self.__height - 1)):
                    symbol += '\n'

            return symbol

    def __repr__(self) -> str:
        ''' Returns a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        '''
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self) -> None:
        ''' Deletes an instance of the Rectangle object
            and prints a message (Bye rectangle...)
        '''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Compare the areas of two rectangles
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
