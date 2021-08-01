# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:21:44 2020

@author: OCAC
"""

string=input("Enter A String:")
isPalindrome=True
for ch in range(0,len(string)//2):
    if string[ch]!=string[len(string)-ch-1]:
        isPalindrome=False
        
if isPalindrome:
    print(f"{string} Is palindrome")
else:
    print(f"{string} Is Not palindrome")
   