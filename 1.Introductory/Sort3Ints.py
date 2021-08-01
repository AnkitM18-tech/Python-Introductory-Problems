# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:23:10 2020

@author: OCAC
"""
a=int(input("Enter 1st No:"))
b=int(input("Enter 2nd No:"))
c=int(input("Enter 3rd No:"))

mx=max(a,b,c)
mn=min(a,b,c)
md=a+b+c-mn-mx

print("mn,md,mx:",mn,md,mx)