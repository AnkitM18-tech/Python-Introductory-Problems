# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 02:20:50 2020

@author: OCAC
"""

char=input("Enter Your Alphabet:")

if char.lower() in "aeiou":
    print("Entered Alphabet is a Vowel")
elif char.lower()=="y":
    print("Sometimes \"y\" is a vowel,and sometimes a consonant")
else:
    print("Entered Alphabet is a Consonant")