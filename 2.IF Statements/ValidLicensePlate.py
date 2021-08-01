# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 02:16:37 2020

@author: OCAC
"""
plate=input("Enter The License Plate Number:")

if len(plate)==6 and plate[0]>="A" and plate[0]<="Z" and\
                        plate[1]>="A" and plate[1]<="Z" and\
                        plate[2]>="A" and plate[2]<="Z" and\
                        plate[3]>="0" and plate[3]<="9" and\
                        plate[4]>="0" and plate[4]<="9"and\
                        plate[5]>="0" and plate[5]<="9" :
                            print(f"The License Plate: {plate} Is Valid for Older Style" )
                            
elif len(plate)==7 and plate[0]>="A" and plate[0]<="Z" and\
                        plate[1]>="A" and plate[1]<="Z" and\
                        plate[2]>="A" and plate[2]<="Z" and\
                        plate[3]>="0" and plate[3]<="9" and\
                        plate[4]>="0" and plate[4]<="9"and\
                        plate[5]>="0" and plate[5]<="9" and\
                        plate[6]>="0" and plate[6]<="9" :
                            print(f"The License Plate: {plate} Is Valid for Newer Style" )
else:
    print(f"The License Plate: {plate} is Not Valid for either styles")