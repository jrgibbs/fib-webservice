__author__ = 'jgibbs'

import unittest
from fib_function import fib

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = [0, 1, 1, 2, 3, 5]

    def test_something(self):
        result = fib(6)
        print result
        self.assertEqual(self.seq, result)


if __name__ == '__main__':
    unittest.main()
