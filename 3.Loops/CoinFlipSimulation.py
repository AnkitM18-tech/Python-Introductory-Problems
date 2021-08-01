# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:01:38 2020

@author: OCAC
"""
import random
counter=0
count=0
total_count=0
result=""
for i in range(10):
    while counter<=2:
        toss=random.choice(["H","T"])
        print(toss,end=" ")
        count+=1
        if toss==result:  
            counter+=1
            
        if toss=="H" or toss=="T":
            result=toss
        print("\t",count,"flips")
        print()
    total_count+=count

avg=total_count/10
print("On average,",avg,"flips were needed")