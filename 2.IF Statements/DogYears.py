# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:16:45 2020

@author: OCAC
"""

HumanYears=int(input("Enter The Human Years:"))
dogYears=0

if HumanYears>2:
    dogYears=(2*10.5)+(HumanYears-2)*4
    print(f"The Equivalent Dog Years is {dogYears} for {HumanYears} human years")
elif HumanYears<=2 and HumanYears>0:
    dogYears=10.5*HumanYears
    print(f"The Equivalent Dog Years is {dogYears} for {HumanYears} human years")
if HumanYears<0:
    print("Negative numbers are not allowed")
    