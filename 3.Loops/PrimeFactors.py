# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:19:52 2020

@author: OCAC
"""

num=int(input("Enter An Integer:"))
factor=2
print("The prime factors of %d is:"%num)
while factor<=num:
    if num%factor==0:
        num//=factor
        print(factor)
    else:
        factor+=1