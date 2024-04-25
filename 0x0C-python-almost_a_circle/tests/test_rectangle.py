#!/usr/bin/python3
""" Rectangle test module """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_1st(unittest.TestCase):
    def setUp(self):
        """ Setup method """
        print("Testing Rectangle")

    def test_width(self):
        """ Test width """
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)

    def test_height(self):
        """ Test height """
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.height, 5)

    def test_no_param(self):
        """ Test no parameter """
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_1_param(self):
        """ Test one parameter """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3)

    def test_rect_from_base(self):
        """ Check for instances """
        self.assertIsInstance(Rectangle(4, 5), Base)

    def test_x(self):
        """ Test x """
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.x, 0)

    def test_x_2(self):
        """ Test x again """
        r2 = Rectangle(4, 5, 5)
        self.assertEqual(r2.x, 5)

    def test_y(self):
        """ Test y """
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.y, 0)

    def test_y_2(self):
        """ Test y again """
        r2 = Rectangle(4, 5, 7, 8)
        self.assertEqual(r2.y, 8)

    def test_all_param(self):
        """ Test all parameters """
        r2 = Rectangle(4, 5, 7, 8, 9)
        self.assertEqual(9, r2.id)

    def test_width_private(self):
        """ Check for privacy of width """
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__width

    def test_height_private(self):
        """ Check for privacy of height """
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__height

    def test_x_private(self):
        """ Check for privacy of x """
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__x

    def test_y_private(self):
        """ Check for privacy of y """
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__y


if __name__ == "__main__":
    unittest.main()
