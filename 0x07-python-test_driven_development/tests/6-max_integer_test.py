#!/usr/bin/python3
''' Unit test for max_integer function '''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        ''' Test integers
        '''
        test_param = [2, 5, 16]
        result = max_integer(test_param)
        self.assertEqual(result, 16)

    def test_max_float(self):
        ''' Test floats
        '''
        test_param = [2.9, 4.5,  5.0, 9.8]
        result = max_integer(test_param)
        self.assertEqual(result, 9.8)

    def test_neg_int1(self):
        ''' Test negative integers '''
        test_param = [-5, -20, -30, -10]
        result = max_integer(test_param)
        self.assertEqual(result,  -5)

    def test_neg_int2(self):
        ''' Test a mixture of positive and negative integers '''
        test_param = [1, 2, -3, 10]
        result = max_integer(test_param)
        self.assertEqual(result, 10)

    def test_one_element(self):
        ''' Test one element
        '''
        test_param = [90]
        result = max_integer(test_param)
        self.assertEqual(result, 90)

    def test_for_string(self):
        ''' Test strings
        '''
        test_param = ""
        result = max_integer(test_param)
        self.assertEqual(result, None)

    def test_max_int_mid(self):
        """ Testing the function for max integer
        """
        test_param = [19, 500, 450]
        result = max_integer(test_param)
        self.assertEqual(result, 500)


if __name__ == "__main__":
    unittest.main()
