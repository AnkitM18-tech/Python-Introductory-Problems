# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:58:13 2020

@author: OCAC
"""

day2sec=86400
hours2sec=3600
min2sec=60

days=int(input("Enter The No of days:"))
hours=float(input("Enter The No of Hours:"))
minutes=float(input("Enter The No of Minutes:"))
seconds=float(input("Enter The No of Seconds:" ))

duration=(days*day2sec)+(hours*hours2sec)+(minutes*min2sec)+seconds

print("The Total Duration in Seconds is",duration)