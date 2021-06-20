#!/usr/bin/python

import unittest
import main

class TestMain(unittest.TestCase):

    def test_root_returns_empty_dict(self):
        self.assertDictEqual(main.null_api_data(), {})

    def test_tds_return_from_just_brix(self):
        response = main.conversion(brix=12)
        self.assertEqual(response["TDS"],  10.2)

    def test_ratio_no_brix(self):
        # We should return a reduced ratio without the need for
        # brix/TDS.
        dose = 19
        beverage = 40
        response = main.conversion(dose=dose, beverage=beverage)
        self.assertEqual(response["Ratio"], 2.10)
    
    def test_ratio_null_if_missing_data(self):
        # a drink ratio is input:output (or flipped, if you feel so inclined)
        # so without either, this should fail.
        response_no_dose = main.conversion(beverage=40)
        response_no_bev = main.conversion(dose=19)
        self.assertIsNone(response_no_dose["Ratio"])
        self.assertIsNone(response_no_bev["Ratio"])

    def test_ey_given_all_data(self):
        dose = 19
        beverage = 40
        brix = 12
        response = main.conversion(dose=dose, beverage=beverage, brix=brix)
        self.assertEqual(response["Extraction Yield"], 21.47)