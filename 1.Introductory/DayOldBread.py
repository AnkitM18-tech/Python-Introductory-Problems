# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:32:34 2020

@author: OCAC
"""
pricefor1=3.49
discount=0.60
breadLoaves=int(input("Enter no of Loaves of day old bread:"))
regularPrice=pricefor1*breadLoaves
discountPrice=regularPrice*discount
totalPrice=regularPrice-discountPrice

print("Regular Price:     %5.2f"%regularPrice)

print("Discount Price:    %5.2f"%discountPrice)

print("Total Price:       %5.2f"%totalPrice)