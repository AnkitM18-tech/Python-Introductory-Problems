# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:11:34 2020

@author: OCAC
"""

rowNo=int(input("Enter The No Of Rows:"))
boolean=str(input("Enter Boolean value(True/False):"))
if boolean=="True":
    for i in range(1,rowNo+1):
        j=1
        while j<=i:
            print("*",end="")
            j+=1
        print()
else:
    for i in range(1,rowNo+1):
        j=rowNo
        while j>=i:
            print("*",end="")
            j-=1
        print()

    