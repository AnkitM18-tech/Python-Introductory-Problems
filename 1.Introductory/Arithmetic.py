# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:58:59 2020

@author: OCAC
"""

from math import log10

a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))

op=input("Enter the operator:")

if op=="+":
    print(a,op,b, ":",(a+b))
    
if op=="-":
    print(a,op,b, ":",(a-b))
    
if op=="*":
    print(a,op,b, ":",(a*b))
    
if op=="/":
    print(a,op,b ,":",(a/b))
    
if op=="%":
    print(a,op,b ,":",(a%b))
    
if op=="^":
    print(a,op,b, ":",(a**b))
    
if op=="log10":
    print(op,a ,":",log10(a))
    