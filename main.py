#!/usr/bin/python

from typing import Optional
from fastapi import FastAPI
from coffee_calc import CoffeeCalc

api = FastAPI()

@api.get("/")
def null_api_data():
    return {}

@api.get("/api/")
def conversion(
    brix: Optional[float] = None, 
    dose: Optional[float] = None, 
    beverage: Optional[float] = None):

    cc = CoffeeCalc()
    conv_dict = {}
    if brix:
        tds = cc.get_tds(brix)
    else:
        tds = None
    conv_dict["TDS"] = tds
    if (dose and beverage):
        ratio =  cc.get_reduced_ratio(dose, beverage)
    else:
        ratio = None
    conv_dict["Ratio"] = ratio
    if (brix and dose and beverage):
        ey = cc.get_extraction_yield(dose, beverage, cc.get_tds(brix))
    else:
        ey = None
    conv_dict["Extraction Yield"] = ey
    return conv_dict
