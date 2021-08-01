# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:38:44 2020

@author: OCAC
"""

def median(a,b,c):
    endNum=max(a,b,c)
    firstNum=min(a,b,c)
    return ((a+b+c)-endNum-firstNum)

def main():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=int(input("Enter Third Number:"))
    result=median(a,b,c)
    print(result,"is the median of the three numbers")
    
main()