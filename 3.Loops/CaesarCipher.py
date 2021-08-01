# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 02:43:58 2020

@author: OCAC
"""

message=input("Enter The Message You Want to Convey:")
shift=int(input("Enter The Shift Amount:"))

newMessage=""

for ch in message:
    if ch>="a" and ch<="z":
        pos=ord(ch)-ord("a")            #ord makes character to ASCII
        pos=(pos+shift)%26
        new_char=chr(pos+ord("a"))
        newMessage+=new_char
    elif ch>="A" and ch<="Z":
        pos=ord(ch)-ord("A")
        pos=(pos+shift)%26
        new_char=chr(pos+ord("A"))      #chr makes ASCII to character
        newMessage+=new_char
    else:
        newMessage+=ch
        
print("The Shifted Message is :",newMessage)