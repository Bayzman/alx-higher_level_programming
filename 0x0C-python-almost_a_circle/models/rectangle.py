#!/usr/bin/python3
''' The class Rectangle inherits from the class Base '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Instantiate the class '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, w):
        ''' width setter '''
        if not isinstance(w, int):
            raise TypeError('width must be an integer')
        if (w <= 0):
            raise ValueError('width must be > 0')
        self.__width = w

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, h):
        ''' height setter '''
        if not isinstance(h, int):
            raise TypeError('height must be an integer')
        if (h <= 0):
            raise ValueError('height must be > 0')
        self.__height = h

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, val):
        ''' x setter '''
        if not isinstance(val, int):
            raise TypeError('x must be an integer')
        if (val < 0):
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, val):
        ''' y setter '''
        if type(val) != int:
            raise TypeError('y must be an integer')
        if (val < 0):
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        ''' Compute area of a rectangle '''
        return (self.width * self.height)

    def display(self):
        ''' Prints the Rectangle instance with the character # '''
        for i in range(self.y):
            print('')
        for j in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            print('#' * self.width, end='')
            print('')

    def __str__(self):
        ''' Overwrites the print method '''
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}')

    def update(self, *args, **kwargs):
        ''' update rectangle to deal with arguments (args) and keyword args (kwargs)
        '''
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
        ''' Returns dictionary representation of a rectangle '''
        to_dict = dict(x=self.x, y=self.y, id=self.id,
                       height=self.height, width=self.width)
        return to_dict
