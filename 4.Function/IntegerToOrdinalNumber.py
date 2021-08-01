# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:34:47 2020

@author: OCAC
"""

def ItO(num):
    if num=="1":
        return "First"
    elif num=="2":
        return "Second"
    elif num=="3":
        return "Third"
    elif num=="4":
        return "Fourth"
    elif num=="5":
        return "Fifth"
    elif num=="6":
        return "Sixth"
    elif num=="7":
        return "Seventh"
    else:
        return ""
    
def main():
    num=input("Enter The Number:")
    ordinal=ItO(num)
    print("The Ordinal Value of the entered no is:",ordinal)
    
main()