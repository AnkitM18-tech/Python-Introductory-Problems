# -*- coding: utf-8 -*-

def smallestno(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if(arr[i]<smallest):
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selectionSort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest=smallestno(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selectionSort([5,7,2,9,1,6]))
            