__author__ = 'jgibbs'

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = [0, 1, 1, 2, 3, 5]

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
