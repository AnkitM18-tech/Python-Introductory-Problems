# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 02:44:08 2020

@author: OCAC
"""

days31=["January","March","May","July","August","October","December"]
days28=["February"]
days30=["April","June","September","November"]

month=input("Enter The Name Of the Month:")

if month.title() in days31:
    print("The No Of Days Are: 31")
elif month.title() in days30:
    print("The No of Days Are:30")
else:
    print("The No of Days Are:28 or 29")