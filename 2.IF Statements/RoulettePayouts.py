# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 03:17:43 2020

@author: OCAC
"""
import random
green=[0,37]
red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

number=random.choice(green+red+black)
if number==37:
    print("The Spin Resulted in: 00")
else:
    print("The Spin Resulted in:",number)

if number in green:
    if number==37:
        print("Pay 00")
    else:
        print("Pay ",number)
    
elif number in red:
    print("Pay ",number)
    print("Pay Red")
   
else:
    print("Pay ",number)
    print("Pay Black")

if number not in green:   
    if number%2==0:
        print("Pay Even")
    else:
        print("Pay Odd")
    
    if number>1 and number<19:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")