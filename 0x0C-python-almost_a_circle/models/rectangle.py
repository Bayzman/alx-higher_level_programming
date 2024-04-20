#!/usr/bin/python3

""" Rectangle class inherits from Base """
from base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter function """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter function """
        self.__width = width

    @property
    def height(self):
        """ Getter function """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter function """
        self.__height = height

    @property
    def x(self):
        """ Getter function """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter function """
        self.__x = x

    @property
    def y(self):
        """ Getter function """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter function """
        self.__y = y
