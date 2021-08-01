# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:51:02 2020

@author: OCAC
"""

decimal=int(input("Enter the Decimal Number:"))

binary=""

while decimal!=0:
    r=decimal%2
    r=str(r)
    binary+=r
    decimal//=2
    
def reverse_slicing(binary):
    return binary[::-1]
binary=reverse_slicing(binary)
print("The Binary Equivalent is:",binary)