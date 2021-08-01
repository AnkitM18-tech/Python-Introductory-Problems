# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 02:48:55 2020

@author: OCAC
"""

Month=input("Enter Your Birth month:")
Day=int(input("Enter Your Birth Date:"))

if Month.title()=="December":
    if Day<=22:
        print("Sagittarius")
    else:
        print("Capricorn")
        
if Month.title()=="January":
    if Day<=19:
        print("Capricorn")
    else:
        print("Aquarius")
        
if Month.title()=="February":
    if Day<=18:
        print("Aquarius")
    else:
        print("Pisces")
        
if Month.title()=="March":
    if Day<=20:
        print("Pisces")
    else:
        print("Aries")
        
if Month.title()=="April":
    if Day<=19:
        print("Aries")
    else:
        print("Taurus")
        
if Month.title()=="May":
    if Day<=20:
        print("Taurus")
    else:
        print("Gemini")
        
if Month.title()=="June":
    if Day<=20:
        print("Gemini")
    else:
        print("Cancer")
        
if Month.title()=="July":
    if Day<=22:
        print("Cancer")
    else:
        print("Leo")
        
if Month.title()=="August":
    if Day<=22:
        print("Leo")
    else:
        print("Virgo")
        
if Month.title()=="September":
    if Day<=22:
        print("Virgo")
    else:
        print("Libra")
        
if Month.title()=="October":
    if Day<=22:
        print("Libra")
    else:
        print("Scorpio")
        
if Month.title()=="November":
    if Day<=21:
        print("Scorpio")
    else:
        print("Sagittarius")
        
