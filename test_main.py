from .main import fun
import math
import unittest


class TestMain(unittest.TestCase):

    def test_with_two_positives(self):
        self.assertEqual(fun.multiply_with_loop(17,19), 17*19)


