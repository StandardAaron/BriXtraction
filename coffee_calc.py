#!/usr/bin/python

class CoffeeCalc:
    def __init__(self):
        pass

    def get_tds(self, brix):
        """
        input: brix - int or float
        output: tds - float
        """
        return float(brix * 0.85)

    def get_reduced_ratio(self, coffee_in, coffee_out):
        return round((coffee_out/coffee_in), 1)
    
    def get_extraction_yield(self, coffee_in, coffee_out, tds):
        """
        inputs:
            coffee_in - int or float
            coffee_out - int or float
            tds - float
        output: ey - float
        
        Extraction yield should be a float with two decimal places always,
        and represents a %.
        """
        extraction_yield = round((coffee_out * tds / coffee_in), 2)
        return extraction_yield