# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:32:19 2020

@author: OCAC
"""

def insert(arr,pos,val):
    i=pos-1
    while i>=0 and arr[i]>val:
        arr[i+1]=arr[i]
        i-=1
    arr[i+1]=val
    return arr
  
    
def sorting(arr):
    for i in range(len(arr)):
        insert(arr,i,arr[i])
        
    return arr

array=[1,4,8,9,11,15,12,13,6]
print(sorting(array))
print(insert(array,6,7))