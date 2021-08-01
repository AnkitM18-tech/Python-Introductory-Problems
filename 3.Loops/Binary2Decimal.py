# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:38:03 2020

@author: OCAC
"""

binary=(input("Enter The Binary Number:"))
exp=len(binary)-1
decimal=0
for num in binary:
    if exp>=0:
        decimal+=int(num)*(2**exp)
        exp-=1
    
print("The Decimal Equivalent is:",decimal)

