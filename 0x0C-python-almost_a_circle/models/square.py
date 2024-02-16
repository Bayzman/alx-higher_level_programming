#!/usr/bin/python3
''' Square inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square inherits from Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Instantiate the class '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size getter '''
        return (self.width)

    @size.setter
    def size(self, val):
        ''' size setter '''
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        ''' Update the class '''
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i in range(len(args)):
                if (i == 0):
                    self.id = args[0]
                elif (i == 1):
                    self.size = args[1]
                elif (i == 2):
                    self.x = args[2]
                elif (i == 3):
                    self.y = args[3]

    def __str__(self):
        ''' Overwrites the print method '''
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}')

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Square '''
        to_dict = {'id': self.id, 'x': self.x,
                   'size': self.size, 'y': self.y}
        return to_dict
