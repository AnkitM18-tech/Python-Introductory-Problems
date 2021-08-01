# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:59:13 2020

@author: OCAC
"""

num=float(input("Enter the Number:"))
guess=num/2

eps=10**-12


while abs((guess**2)-num)>eps:
    guess=(guess+(num/guess))/2
    
print("The Approximate Square Root Of The %f is :%.4f"%(num,guess))