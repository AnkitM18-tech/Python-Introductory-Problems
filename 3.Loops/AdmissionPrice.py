# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:10:27 2020

@author: OCAC
"""
charge3_12=14.00
charge65=18.00
chargeOthers=23.00

print("Welcome to The Zoo!Enter Group members Age one by one")
age=input("Enter The Age Of The Person(blank to quit):")
total=0
i=0
while age!="":
    age=int(age)
    if age<=2:
        charge=0
    elif age>=3 and age<=12:
        charge=charge3_12
    elif age>=65:
        charge=charge65
    else:
        charge=chargeOthers
        
    total+=charge
    i+=1
    age=input("Enter The Age Of The Person(blank to quit):")
    
if total!=0:   
    print("The Charge For The Current Group of %d people is %.02f:"%(i,total))
else:
    print("No Age Entered!The System Expects New Group")