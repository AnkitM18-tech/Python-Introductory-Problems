# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:21:02 2020

@author: OCAC
"""
interest=0.04
Principal_amount=float(input("Enter The Amount Deposited:"))
Amount_after1year=Principal_amount*(1+interest)
Amount_after2years=Principal_amount*((1+interest)**2)
Amount_after3years=Principal_amount*((1+interest)**3)

print("The Amount after 1year: %.2f" %Amount_after1year)
print("The Amount after 2years: %.2f" %Amount_after2years)
print("The Amount after 3years: %.2f" %Amount_after3years)