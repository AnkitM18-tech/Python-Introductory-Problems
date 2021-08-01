# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:34:11 2020

@author: OCAC
"""
tax_rate=0.18
tip_rate=0.18
mealCost=float(input("Enter The Cost of the Meal: "))
taxAmt=tax_rate*mealCost
tipAmt=tip_rate*mealCost
grandtotal=mealCost+taxAmt+tipAmt
print("The Total Amount to be paid=%.2f with %.2f tax and %.2f tip" %\
      (grandtotal,taxAmt,tipAmt))