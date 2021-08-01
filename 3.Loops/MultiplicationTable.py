# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:09:03 2020

@author: OCAC
"""

Min=1
Max=10

print("    ",end="")
for i in range(Min,Max+1):
    print("%4d"%i,end="")
print()

for i in range(Min,Max+1):
    print("%4d"%i,end="")
    for j in range(Min,Max+1):
        print("%4d"%(i*j),end="")
    print()