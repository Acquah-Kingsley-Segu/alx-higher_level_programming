#!/usr/bin/python3
""" Unittest for max_integer([..])"""



import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Group of individual test cases """
    def test_max_integer_no_param(self):
        self.assertEqual(max_integer(), None)
    def test_max_integer_normal(self):
        self.assertEqual(max_integer([3, 0, 2, 99]), 99)
