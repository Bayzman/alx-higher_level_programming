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
        self.assertEqual(r2.id, 9)

    def setUp(self):
        self.rectangle = Rectangle(10, 5, 1, 1, 1)

    def test_init(self):
        """ Test init """
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 1)
        self.assertEqual(self.rectangle.id, 1)

    def test_width_getter(self):
        """ Test width getter """
        self.assertEqual(self.rectangle.width, 10)

    def test_width_setter(self):
        """ Test width setter """
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_height_getter(self):
        """ Test height getter """
        self.assertEqual(self.rectangle.height, 5)

    def test_height_setter(self):
        """ Test height setter """
        self.rectangle.height = 3
        self.assertEqual(self.rectangle.height, 3)

    def test_x_getter(self):
        """ Test x getter """
        self.assertEqual(self.rectangle.x, 1)

    def test_x_setter(self):
        """ Test x setter """
        self.rectangle.x = 2
        self.assertEqual(self.rectangle.x, 2)

    def test_y_getter(self):
        """ Test y getter """
        self.assertEqual(self.rectangle.y, 1)

    def test_y_setter(self):
        """ Test y setter """
        self.rectangle.y = 3
        self.assertEqual(self.rectangle.y, 3)

    def test_area(self):
        """ Test area """
        self.assertEqual(self.rectangle.area(), 50)

    def test_display(self):
        """ Test display """
        self.rectangle.display()

    def test_str(self):
        """ Test __str__ """
        self.assertEqual(str(self.rectangle), '[Rectangle] (1) 1/1 - 10/5')

    def test_update(self):
        """ Test update """
        self.rectangle.update(89, 5, 3, 4)
        self.assertEqual(self.rectangle.id, 89)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 1)

    def test_to_dict(self):
        """ Test dict """
        to_dict = self.rectangle.to_dictionary()
        self.assertIn('x', to_dict)
        self.assertIn('y', to_dict)
        self.assertIn('id', to_dict)
        self.assertIn('height', to_dict)
        self.assertIn('width', to_dict)


if __name__ == "__main__":
    unittest.main()
