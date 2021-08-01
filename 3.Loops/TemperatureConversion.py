# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:32:51 2020

@author: OCAC
"""

cel=0
print("Celsius Scale\t\t\tFahrenheit Scale\n")
while cel%10==0 and (cel>=0 and cel<=100):
    fahr=((9/5)*cel)+32
    print("%d\t\t\t\t%d\n"%(cel,fahr))
    cel+=10
    