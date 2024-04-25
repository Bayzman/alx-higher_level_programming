#!/usr/bin/python3
""" Test Base Module """
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base Module """
    b1 = Base()
    b2 = Base()
    b3 = Base()

    def test_no_param_1_instance(self):
        """ Test with no parameters """
        self.assertEqual(self.b1.id, 1)
        # b2.id should be 2 but because it has been assigned to 6
        # in test_assign_new_id, b2.id != 2
        self.assertEqual(self.b2.id, 6)
        self.assertEqual(self.b3.id, 3)

    def test_with_param(self):
        """ Test with parameter """
        self.b4 = Base(3)
        self.assertEqual(self.b4.id, 3)

    def test_none_param(self):
        """ Test with None """
        self.b5 = Base(None)
        self.assertEqual(self.b5.id, 4)

    def test_assign_new_id(self):
        """ Assign new id """
        self.b2.id = 6
        self.assertEqual(self.b2.id, 6)

    def test_bool_param(self):
        """ Test with boolean parameter """
        b6 = Base(True)
        self.assertNotEqual(b6.id, False)

    def test_isisnstance(self):
        """ Check for instances """
        b5 = Base(5)
        self.assertIsInstance(b5, Base)

    def test_privacy(self):
        """ Check privacy of class object """
        with self.assertRaises(AttributeError):
            Base().__nb_objects

if __name__ == '__main__':
    unittest.main()
