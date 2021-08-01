# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:43:40 2020

@author: OCAC
"""
import math
print("Enter The Values Of a ,b & c in The Equation\" ax^2+bx+c \":\n")
a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
D=((b**2)-(4*a*c))

if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print("The No Of Real Roots is 2 and values are %d & %d"%(root1,root2))
elif D==0:
    root1=-b/(2*a)
    root2=0
    print("The No Of Real Roots is 1 and value is %d"%root1)
else:
    print("No Real Roots")
    


