# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:29:08 2020

@author: OCAC
"""

pennies_per_nickel=5
nickel=0.05

total=0.00

price=(input("Enter The Price Of The Item (blank to quit):"))

while price!="":
    total+=float(price)
    price=(input("Enter The Price Of The Next Item (blank to quit):"))
    
print("The Exact Amount Payable is %.2f"%total)
    
roundingInd=total*100%pennies_per_nickel     #total no of pennies
    
if roundingInd<pennies_per_nickel/2:
    cash_total=total-roundingInd/100
else:
    cash_total=total+nickel-roundingInd/100
    
print("The Cash Amount Payable is%.02f"%cash_total)