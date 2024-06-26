#!/usr/bin/python3
""" Square Test Module """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Test cases """
    def setUp(self):
        """ Setup test """
        self.square = Square(10, 1, 1, 1)

    def test_init(self):
        """ Test constructor """
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 1)
        self.assertEqual(self.square.id, 1)

    def test_size_getter(self):
        """ Test getter """
        self.assertEqual(self.square.size, 10)

    def test_size_setter(self):
        """ Test setter """
        self.square.size = 5
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)

    def test_update(self):
        """ Test update """
        self.square.update(89, 2, 3)
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 1)

    def test_update_kwargs(self):
        """ Test kwargs """
        self.square.update(size=5, x=4, y=5)
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

    def test_to_dict(self):
        """ Test to dictionary """
        to_dict = self.square.to_dictionary()
        self.assertIn('id', to_dict)
        self.assertIn('x', to_dict)
        self.assertIn('size', to_dict)
        self.assertIn('y', to_dict)

    def test_str(self):
        """ Test __str__ """
        self.assertEqual(str(self.square), '[Square] (1) 1/1 - 10')

    def test_x_private(self):
        """ Privacy test """
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__x

    def test_y_private(self):
        """ Privacy test """
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__y


if __name__ == '__main__':
    unittest.main()
