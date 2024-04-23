#!/usr/bin/python3

""" Rectangle class inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter function """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter function """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if (width <= 0):
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ Getter function """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter function """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if (height <= 0):
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ Getter function """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter function """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if (x < 0):
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ Getter function """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter function """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if (y < 0):
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Computes the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints the Rectangle instance with the character # """
        for _ in range(self.y):
            print("")

        for i in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """ Overwrite the __str__ method """
        out = f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
                {self.width}/{self.height}'
        return out

    def update(self, *args, **kwargs):
        """ Supports no-keyword and key-worded arguments """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                if (i == 0):
                    self.id = args[0]
                elif (i == 1):
                    self.width = args[1]
                elif (i == 2):
                    self.height = args[2]
                elif (i == 3):
                    self.x = args[3]
                elif (i == 4):
                    self.y = args[4]

    def to_dictionary(self):
        """ Returns dictionary representation of a rectangle instance """
        to_dict = dict(x=self.x, y=self.y, id=self.id,
                       height=self.height, width=self.width)
        return to_dict
