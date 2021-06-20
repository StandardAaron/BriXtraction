#!/usr/bin/python
import unittest
from coffee_calc import CoffeeCalc

class TestBrixConverter(unittest.TestCase):
    """
    Tests all the functions in our conversion class, which backs the API
    responses in our Main app.
    """
    def setUp(self):
        self.cc = CoffeeCalc()

    def test_tds_takes_float_or_int(self):
        # make sure get_tds() works with either a float or
        # an integer.
        i = 11
        f = 11.0
        tds_i = self.cc.get_tds(i)
        tds_f = self.cc.get_tds(f)
        self.assertEqual(tds_i, tds_f)

    def test_return_tds_is_less_than_brix(self):
        # TDS readings should never be more than the brix reading,
        # if it's higher, something is broken.
        brix = 10
        tds = self.cc.get_tds(brix) 
        self.assertLess(tds, brix)

    def test_reduced_ratio_decimal_place(self):
        # Make sure we always get tenths place decimal
        self.assertEqual(self.cc.get_reduced_ratio(21.5, 324), 15.1)
        self.assertEqual(self.cc.get_reduced_ratio(16, 256), 16.0)

    def test_get_extraction_yield_decimal_place(self):
        self.assertEqual(self.cc.get_extraction_yield(19, 40, 11.049999999999999), 23.26)
