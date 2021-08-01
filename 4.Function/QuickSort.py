# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:53:45 2020

@author: OCAC
"""

def sort(arr):
    if len(arr)<2:
        return arr
    else:
         pivot=arr[0]
         greater=[i for i in arr[1:] if i>pivot]
         less=[i for i in arr[1:] if i<=pivot]
         return sort(less)+[pivot]+sort(greater)

#arr=array(input("Enter The Array:"))
print(sort([12,34,2,67,23,1,4,5]))