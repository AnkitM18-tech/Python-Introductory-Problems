# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:23:00 2020

@author: OCAC
"""

from math import pi

r=float(input("Enter The Radius Value:"))

area_circle=pi*(r**2)
volume_sphere=4/3*pi*(r**3)

print("The area of the circle is %.2f"%area_circle,\
      " and The volume of the sphere is %.2f"%volume_sphere )