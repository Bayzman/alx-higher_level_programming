#!/usr/bin/python3

""" Square inherits from rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter function """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Size  setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the class attributes """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Overwrites the print method """
        out = f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
        return out

    def to_dictionary(self):
        """ Returns dictionary representation of a square instance """
        to_dict = {'id': self.id, 'x': self.x,
                   'size': self.size, 'y': self.y}
        return to_dict
