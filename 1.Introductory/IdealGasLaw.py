# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:20:16 2020

@author: OCAC
"""

P=float(input("Enter The Pressure(in Pascals):"))
V=float(input("Enter The Volume(in Liters):"))
R=8.314
t=float(input("Enter The Temperature(in Celsius):"))
T=t+273.15
n=(P*V)/(R*T)
print("The no of moles of gas=",n,"moles")