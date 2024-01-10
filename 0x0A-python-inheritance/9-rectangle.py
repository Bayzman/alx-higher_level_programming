#!/usr/bin/python3
''' Rectangle class that inherits from BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class '''
    def __init__(self, width, height):
        ''' Instantiate the class
        Args:
            width (int): width
            height (int): height
        '''
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        ''' Calculate the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' Magic method to overwrite print '''
        return (f'[Rectangle] {self.__width}/{self.__height}')
