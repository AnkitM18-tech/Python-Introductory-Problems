# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:52:13 2020

@author: OCAC
"""
import math
s=float(input("Enter The Side Length:"))
n=float(input("Enter The No of sides:"))

area=(n*(s**2))/(4*math.tan(math.pi/n))
print("The area of the Polygon:",area)