# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:38:14 2020

@author: OCAC
"""

Ta=float(input("Enter The Air Temperature(in celsius):"))
V=float(input("Enter The Wind Speed(in KMPH):"))

WCI=round(13.12+(0.6215*Ta)-(11.37*(V**0.16))+(0.3965*Ta*(V**0.16)))

print("THE WCI is:",WCI)