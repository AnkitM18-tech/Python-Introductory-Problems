# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:23:23 2020

@author: OCAC
"""

import random
num=random.randint(1,101)
Max=num
print(Max)
updates=0
for i in range(99):
    num=random.randrange(1,101)
    if num>Max:
        Max=num
        updates+=1
        print(num,"<==update")
    else:
        print(num)
print("The Maximum Value Found was:",Max)
print("The Maximum Value Was Updated %d times"%updates)