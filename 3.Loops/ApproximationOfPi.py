# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 01:03:07 2020

@author: OCAC
"""

baseValue=3
noOfapproximation=15
i=2
j=-1
n=0
piValue=0
factor=4/(i*(i+1)*(i+2))
baseValue+=(j**n)*factor
piValue+=baseValue
print("Approximation Value 1 of Pi is:%f"%piValue)
while noOfapproximation!=0:
    i+=2
    factor=4/(i*(i+1)*(i+2))
    n+=1
    piValue+=(j**n)*factor
   
    noOfapproximation-=1
    print("Approximation Value %d of Pi is:%f"%(n+1,piValue))
    