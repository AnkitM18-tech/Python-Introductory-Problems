# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:34:25 2020

@author: OCAC
"""

year=int(input("Enter a Year:"))

if year%12==8:
    animal="Dragon"
elif year%12==9:
    animal="Snake"
elif year%12==10:
    animal="Horse"
elif year%12==11:
    animal="Sheep"
elif year%12==0:
    animal="Monkey"
elif year%12==1:
    animal="Rooster"
elif year%12==2:
    animal="Dog"
elif year%12==3:
    animal="Pig"
elif year%12==4:
    animal="Rat"
elif year%12==5:
    animal="Ox"
elif year%12==6:
    animal="Tiger" 
else:
    animal="Hare"
    
print("The Animal Associated With Year is",animal)