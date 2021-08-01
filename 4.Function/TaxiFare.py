# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 02:15:38 2020

@author: OCAC
"""

baseFare=4.00
extra=0.25
distanceFare=140

def taxifare(distance):
    distance*=1000
    fareDistance=distance/distanceFare
    fare=(fareDistance*extra)+baseFare
    return fare

distance=float(input("Enter The Distance Covered(kms):"))
result=taxifare(distance)
print("The Total Taxi Fare is:%.2f"%result)