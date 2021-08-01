# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 04:21:44 2020

@author: OCAC
"""

year=int(input("Enter The year:"))

if year%400==0:
    isLeapyear=True
elif year%100==0:
    isLeapyear=False
elif year%4==0:
    isLeapyear=True
else:
    isLeapyear=False
    
if isLeapyear:
    print(year,"is a leap year")
else:
    print(year,"is not aleap year")