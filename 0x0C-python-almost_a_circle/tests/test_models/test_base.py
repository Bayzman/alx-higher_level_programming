#!/usr/bin/python3
""" Test Base Module """
import os
import unittest
from models.base import Base


class TestBase_1st(unittest.TestCase):
    def setUp(self):
        """ Setup method """
        self.b = Base()
        self.b1 = Base()
        self.b2 = Base()
        print("Testing Base")

    def test_no_param_1_instance(self):
        """ Test with no parameters """
        self.assertEqual(self.b.id, 1)

    def test_no_param_3_instances(self):
        """ Test multiple instances """
        self.assertEqual(self.b2.id, 3)

    def test_with_param(self):
        """ Test with parameter """
        self.b1 = Base(3)
        self.assertEqual(self.b1.id, 3)

    def test_none_param(self):
        """ Test with None """
        self.b1 = Base(None)
        self.assertEqual(b1.id, 11)

    def test_assign_new_id(self):
        """ Assign new id """
        self.b2.id = 6
        self.assertEqual(self.b2.id, 6)

    def test_bool_param(self):
        """ Test with boolean parameter """
        b3 = Base(True)
        self.assertNotEqual(b3.id, False)

    def test_isisnstance(self):
        """ Check for instances """
        b4 = Base(5)
        self.assertIsInstance(b4, Base)

    def test_privacy(self):
        """ Check privacy of class object """
        with self.assertRaises(AttributeError):
            Base().__nb_objects

if __name__ == '__main__':
    unittest.main()
