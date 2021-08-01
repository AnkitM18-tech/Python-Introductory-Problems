# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:44:34 2020

@author: OCAC
"""

bitString=input("Enter The 8 Bits String(blank to quit):")

while bitString!="" :
    if len(bitString)==8 and bitString.count("0")+bitString.count("1")==8:
        i=bitString.count("1")
    else:
        print("Invalid Bits String")
        bitString=input("Enter The 8 Bits String(blank to quit):")
        
    if i%2==0:
        parityBit=0
    else:
        parityBit=1
        
    print("The Parity Bit For The Entered Bits String %s is:%d"%(bitString,parityBit))
    print("Resultant Bit string is :%s"%(bitString+str(parityBit)))
    
    bitString=input("Enter The 8 Bits String(blank to quit):")

