#!/usr/bin/python3

""" Defines a rectangle """


class Rectangle():
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Class initialization """
        self.width = width
        self.height = height

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
    def height(self, height):
        """ Setter for height """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
