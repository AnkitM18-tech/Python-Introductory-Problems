# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 03:23:37 2020

@author: OCAC
"""

from IntegerToOrdinalNumber2 import ItO

def displayVerse(n):
    print("On The",ItO(n),"day of Christmas")
    print("my true love sent to me:")
    
    if n>=12:
        print("Twelve Drummers Drumming.")
    if n>=11:
        print("Eleven Pipers piping.")
    if n>=10:
        print("Ten Lords a leaping.")
    if n>=9:
        print("Nine ladies dancing.")
    if n>=8:
        print("Eight maids milking.")
    if n>=7:
        print("Seven Swans swimming.")
    if n>=6:
        print("Six Geese a Laying.")
    if n>=5:
        print("Five golden Rings.")
    if n>=4:
        print("Four Calling Birds.")
    if n>=3:
        print("Three French hens.")
    if n>=2:
        print("Two turtle doves.")
    if n==1:
        print("A",end=" ")
    else:
        print("And a",end=" ")
        
    print("patridge in a pear tree.")
    print()
    
    
def main():
    for verse in range(1,13):
        displayVerse(verse)
        
main()
    
    