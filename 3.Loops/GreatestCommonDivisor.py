# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:56:16 2020

@author: OCAC
"""

first_num=int(input("Enter The First Number:"))
second_num=int(input("Enter The Second Number:"))

d=min(first_num,second_num)

while first_num%d!=0 or second_num%d!=0:
    d-=1
    
print("The GCD of %d & %d is:%d"%(first_num,second_num,d))