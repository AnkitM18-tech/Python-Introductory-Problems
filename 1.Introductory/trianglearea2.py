# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:36:23 2020

@author: OCAC
"""
from math import sqrt
s1=float(input("Enter Length of First side:"))
s2=float(input("Enter Length of Second side:"))
s3=float(input("Enter Length of Third side:"))
s=(s1+s2+s3)/2

area=sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("The area of the Triangle is:",area,"cm^2")