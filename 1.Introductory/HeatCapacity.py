# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:34:27 2020

@author: OCAC
"""

s=4.186
elec_cost=8.9
units=2.778*(10**-7)
m=float(input("Enter mass of the water:"))
delT=float(input("Enter the temperature change:"))

q=m*s*delT
print("The Energy Required For The temperature change is %.2f"%q,"Joules")

billing=q*units*(elec_cost/100)

print("The Cost For Boiling cup of water: $ ",billing)
