# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:02:53 2020

@author: OCAC
"""

num=int(input("Enter Your Number:"))

fourth=num//1000
num=num%1000
third=num//100
num=num%100
second=num//10
first=num%10

sumnum=fourth+third+second+first

if sumnum>9:
    sumnum=(sumnum//10)+(sumnum%10)
    
print("The Sum Of Integers In Your Number Is:",sumnum)