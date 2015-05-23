__author__ = 'jgibbs'

import unittest
from fib_function import fib

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = [0, 1, 1, 2, 3, 5]

    def test_expected_results(self):
        result = fib(6)
        print result
        self.assertEqual(self.seq, result)

    def test_negative_number(self):
        self.assertRaises(Exception, -5)

    def test_float(self):
        self.assertRaises(Exception, 3.14)

    def test_alpha(self):
        self.assertRaises(Exception, "foo")



if __name__ == '__main__':
    unittest.main()
