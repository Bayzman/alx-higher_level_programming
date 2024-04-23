#!/usr/bin/python3
""" Square Test Module """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare_1st(unittest.TestCase):
    def setUp(self):
        """ Setup method """
        print("Testing Square")

    def test_width(self):
        """ Test width """
        s1 = Square(4, 5)
        self.assertEqual(s1.size, 4)

    def test_height(self):
        """ Test height """
        s1 = Square(4, 5)
        self.assertEqual(s1.x, 5)

    def test_no_param(self):
        """ Test no parameter """
        with self.assertRaises(TypeError):
            s2 = Square()

    def test_1_param(self):
        """ Test 1 parameter """
        s3 = Square(3)
        self.assertEqual(s3.size, 3)

    def test_rect_from_base(self):
        """ Check for instances """
        self.assertIsInstance(Square(4, 5), Base)

    def test_x(self):
        """ Test x """
        s3 = Square(4)
        self.assertEqual(s3.x, 0)

    def test_x_2(self):
        """ Test x again """
        s3 = Square(4, 5)
        self.assertEqual(s3.x, 5)

    def test_y(self):
        """ Test y """
        s3 = Square(4, 5)
        self.assertEqual(s3.y, 0)

    def test_y_2(self):
        """ Test y again """
        s3 = Square(4, 5, 7)
        self.assertEqual(s3.y, 7)

    def test_all_param(self):
        """ Test all parameters """
        s3 = Square(4, 5, 7, 9)
        self.assertEqual(9, s3.id)

    def test_size_private(self):
        """ Test for privacy """
        r2 = Rectangle(4, 5, 7, 8)
        with self.assertRaises(AttributeError):
            r2.__size

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
