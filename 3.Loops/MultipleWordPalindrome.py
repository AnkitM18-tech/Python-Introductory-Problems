# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:36:06 2020

@author: OCAC
"""

string=input("Enter The String:")

isPalindrome=True
#string2="".join(string.split())    #clear whitespaces
string2=string.replace(" ","")

for i in range(0,len(string2)//2):
    if string2[i]!=string2[len(string2)-1-i]:
        isPalindrome=False

    
if isPalindrome:
    print(string," is Palindrome")
else:
    print(string," is not Palindrome")