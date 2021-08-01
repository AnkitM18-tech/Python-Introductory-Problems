# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:12:08 2020

@author: OCAC
"""
from math import sqrt
perimeter=0

first_x=float(input("Enter The X Coordinate:"))
first_y=float(input("Enter The Y Coordinate:"))

prev_x=first_x
prev_y=first_y

next_x=input("Enter The Next X Coordinate:")

while next_x!="":
    next_x=float(next_x)
    next_y=float(input("Enter The Next Y Coordinate:"))
    dist=sqrt((next_x-prev_x)**2+(next_y-prev_y)**2)
    perimeter+=dist
    prev_x=next_x
    prev_y=next_y
    next_x=input("Enter The Next X Coordinate(blank to quit):")
    
    
dist=sqrt((first_x-prev_x)**2+(first_y-prev_y)**2)
perimeter+=dist
print("The Perimeter Of The Polygon is:",perimeter)