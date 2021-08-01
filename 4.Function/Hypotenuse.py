# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 02:03:02 2020

@author: OCAC
"""

def pythogorian(b,p):
    from math import sqrt
    h=sqrt(p**2+b**2)
    return h

def main():
    b=float(input("Enter The Base length:"))
    p=float(input("Enter The Perpendicular length:"))
    result=pythogorian(b,p)
    print("The Hypotenuse Length is %.2f"%result)
    
main()