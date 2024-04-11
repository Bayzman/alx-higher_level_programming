#!/usr/bin/python3

""" Unit tests for the max_integer function """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit tests for the max_integer function """

    def test_max_int(self):
        """ Test max_integer on a list of integers """
        max_int = max_integer([1, 2, 3, 4])
        self.assertEqual(max_int, 4)

    def test_max_at_beginning(self):
        """ Test max_integer on a list of integers """
        max_int = max_integer([4, 2, 3, 1])
        self.assertEqual(max_int, 4)

    def test_max_float(self):
        """ Test max_integer on a list of floats """
        max_int = max_integer([5.0, 10.5, 1.5, 4.5, 98.5, 99.9])
        self.assertEqual(max_int, 99.9)

    def test_neg_int(self):
        """ Test max_integer on a list of negative integers """
        max_int = max_integer([-12, -50, -23, -2, -6])
        self.assertEqual(max_int, -2)

    def test_one_element(self):
        """ Test max_integer on a list with only one integer element """
        max_int = max_integer([100])
        self.assertEqual(max_int, 100)

    def test_string(self):
        """ Test max_integer on strings """
        max_int = max_integer("")
        self.assertEqual(max_int, None)


if __name__ == '__main__':
    unittest.main()
