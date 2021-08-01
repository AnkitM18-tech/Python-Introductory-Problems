# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:39:14 2020

@author: OCAC
"""
us_mpg=235.215
FuelEff_US=float(input("Enter Fuel Efficiency Value :"))
FuelEff_Can=FuelEff_US*us_mpg

print("The Equivalent Fuel Efficiency in Canadian Unit :",FuelEff_Can)