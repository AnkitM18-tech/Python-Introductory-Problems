# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:34:59 2020

@author: OCAC
"""
import math
from math import radians
t1=radians(float(input("Enter The Latitude of the first point:")))
g1=radians(float(input("Enter The Longitude of the first point:")))
t2=radians(float(input("Enter The Latitude of the second point:")))
g2=radians(float(input("Enter The Longitude of the second point:")))

distance=6371.01*math.acos((math.sin(t1)*math.sin(t2))+(math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))
print("The Distance between two points is :",distance,"kms")