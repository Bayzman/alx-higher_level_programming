#!/usr/bin/python3

""" Defines a rectangle """


class Rectangle():
    """ Defines a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Class initialization """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Computes the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Computes the perimeter of a rectangle """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Prints rectangles using the # symbol """
        symbol = ''
        if (self.__width == 0 or self.__height == 0):
            return ''
        for i in range(self.__height):
            symbol += (str(self.print_symbol) * self.__width)
            if (i != (self.__height - 1)):
                symbol += '\n'

        return symbol

    def __repr__(self):
        """ Returns a string representation of the rectangle """
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """ Deletes an instance of the Rectangle class """
        print('Bye rectangle...')
        self.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle based on the area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if (rect_1.area() >= rect_2.area()):
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width = height = size """
        return Rectangle(size, size)