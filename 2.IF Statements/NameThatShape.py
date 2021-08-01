# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 02:36:52 2020

@author: OCAC
"""

sides=int(input("Enter The Number Of Sides:"))

if sides==3:
    print("Triangle")
elif sides==4:
    print("Quadrilateral")
elif sides==5:
    print("Pentagon")
elif sides==6:
    print("Hexagon")
elif sides==7:
    print("Heptagon")
elif sides==8:
    print("Octagon")
elif sides==9:
    print("Nonagon")
elif sides==10:
    print("Decagon")
else:
    print("Inappropriate Side Number")
