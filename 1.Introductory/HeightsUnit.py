# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:03:02 2020

@author: OCAC
"""
feet_in_centimetres=12*2.54
inches_in_centimetres=2.54
feets=int(input("Enter The Number of Feets:"))
inches=int(input("Enter The Number of inches:"))

height_in_centimetres=(feets*feet_in_centimetres)+(inches*inches_in_centimetres)
print("The height in Centimeters :",height_in_centimetres)