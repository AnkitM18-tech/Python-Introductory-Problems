# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 02:40:46 2020

@author: OCAC
"""

first_item=10.95
subsequent_item=2.95

def itemCharge(itemsNo):
    fare=first_item+((itemsNo-1)*subsequent_item)
    return fare
def main():
    number_of_items=int(input("Enter The Number Of Items Ordered:"))
    result=itemCharge(number_of_items)
    print("The Shipping Charge For The Ordered Items is:%.2f"%result)
    
main()