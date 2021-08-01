# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:38:56 2020

@author: OCAC
"""

def triangle(a,b,c):
    if a>=b+c or b>=a+c or c>=a+b:
        result=False
        
    else:
        result=True
        
        return result
    
if __name__=="__main__":
    a=float(input("Enter Value Of Side 1:"))
    b=float(input("Enter Value Of Side 2:"))
    c=float(input("Enter Value Of Side 3:"))
    
    boolean=triangle(a,b,c)
    
    if boolean:
        print("Triangle can be Formed" )
        
    else:
        print("Triangle Can Not be Formed")