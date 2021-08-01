# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:18:28 2020

@author: OCAC
"""

li=[]

number=int(input("Enter The Number:"))

if number==0:
    print("First Number Can't be \"0\"")

while number !=0:
    li.append(number)
    avg=sum(li)/len(li)
    number=int(input("Enter The Next Number:"))
    if number==0:
        print("End Of Entering Inputs")
        print("The Average Of The Numbers is: ",avg)
    