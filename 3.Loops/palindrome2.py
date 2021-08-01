# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 00:53:13 2020

@author: OCAC
"""

word=input("Enter a String:")

if word[::-1]==word:
    print("%s is Palindrome"%word)
else:
    print("%s is not Palindrome"%word)