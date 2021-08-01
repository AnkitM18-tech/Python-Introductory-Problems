# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:13:03 2020

@author: OCAC
"""

feets_in_inches=12
feets_in_yards=1/3
feets_in_miles=0.000189

feets=int(input("Enter The number Of feets:"))
inches=feets*1/feets_in_inches
yards=feets*feets_in_yards
miles=feets*feets_in_miles

print(feets,"number of feets is equivalent to %.2f" \
      %inches,"no of inches %.2f,"%yards,"no of yards& %.2f"%miles,"no of miles")