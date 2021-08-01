# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:51:38 2020

@author: OCAC
"""

Temp_Cels=float(input("Enter The Temperature in Celsius:"))

Temp_Fahr=(Temp_Cels*9/5)+32
Temp_Kel=Temp_Cels+273.15

print("The Temperature in Fahrenheit is %.2f Fahrenheit"%Temp_Fahr,\
      " & Temperature in Kelvin is %.2f Kelvin"%Temp_Kel)