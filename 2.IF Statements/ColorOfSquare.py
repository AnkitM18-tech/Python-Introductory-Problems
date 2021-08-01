# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 14:19:35 2020

@author: OCAC
"""
Position=input("Enter The Position:")
Column=Position[0]
Row=Position[1]

if Column in "aceg" and int(Row)%2==1:
    print("The Square is Black")
elif Column in"bdfh" and int(Row)%2==0:
    print("The Square is Black")
else:
    print("The Square is White")
    