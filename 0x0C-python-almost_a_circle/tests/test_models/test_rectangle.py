#!/usr/bin/python3
""" Rectangle test module """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_1st(unittest.TestCase):
    """ Test cases """
    def test_width_height(self):
        """ Test parameters """
        r = Rectangle(4, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

    def test_2_param(self):
        """ Test two parameters """
        r = Rectangle(3, 4)
        self.assertIsInstance(r, Rectangle)

    def test_3_param(self):
        """ Test three parameters """
        r = Rectangle(3, 4, 5)
        self.assertIsInstance(r, Rectangle)

    def test_4_param(self):
        """ Test four parameters """
        r = Rectangle(3, 4, 5, 10)
        self.assertIsInstance(r, Rectangle)

    def test_type_exception1(self):
        """ Check for correct data types """
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)

    def test_type_exception2(self):
        """ Check for correct data types """
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")

    def test_type_exception3(self):
        """ Check for correct data types """
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")

    def test_type_exception4(self):
        """ Check for correct data types """
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")

    def test_value_exception1(self):
        """ Value Error """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_value_exception2(self):
        """ Value Error """
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)

    def test_value_exception3(self):
        """ Value Error """
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)

    def test_value_exception4(self):
        """ Value Error """
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    #def test_update(self):
     #   """ Test update method """
      #  r = Rectangle(1, 2)
       # r.update(10, 15)
        #self.assertEqual(r.width, 10)
        #self.assertEqual(r.height, 15)

    def test_rect_from_base(self):
        """ Check for instances """
        self.assertIsInstance(Rectangle(4, 5), Base)

    def test_area(self):
        """ Test x """
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.area(), 20)

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
