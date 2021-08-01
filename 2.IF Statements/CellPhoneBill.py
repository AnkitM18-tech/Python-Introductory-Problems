# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 01:35:18 2020

@author: OCAC
"""
addMinute=0.25
addMessage=0.15
charge911=0.44
taxRate=0.05
planCost=15

minutes=int(input("Enter The Number Of Minutes:"))
messages=int(input("Enter The Number Of Messages:"))

if minutes>50:
    addMinuteCost=addMinute*(minutes-50)
else:
    addMinuteCost=0
    
if messages>50:
    addMessageCost=addMessage*(messages-50)
else:
    addMessageCost=0
    
Bill=(planCost+charge911+addMinuteCost+addMessageCost)
tax=Bill*taxRate
TotalBill=Bill+tax

print("The Base Charge is :                    %5.2f"%planCost)
if addMinuteCost:
    print("The Additional Minutes Cost is:         %5.2f"%addMinuteCost)

if addMessageCost:
    print("The Additional Messages Cost is:        %5.2f"%addMessageCost)
    
print("The 911 fee is:                         %5.2f"%charge911)
print("The Sales Tax is:                       %5.2f"%tax)
print("The Total Bill is:                      %5.2f"%TotalBill)
