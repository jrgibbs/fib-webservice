__author__ = 'jgibbs'

import unittest
from flask import json
from fib_webservice import app


class FibFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_fib(self):
        result = self.app.get('/fib/6')
        data = json.loads(result.data)
        self.assertEqual(data['sequence'], [0, 1, 1, 2, 3, 5])

    def test_fib_invalid_url(self):
        result = self.app.get('/fib/foo')
        data = json.loads(result.data)
        print(data)
        self.assertEqual(data['code'], 404)

if __name__ == '__main__':
    unittest.main()