# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 04:28:50 2020

@author: OCAC
"""

year=int(input("Enter The Year:"))
month=int(input("Enter The Month:"))
date=int(input("Enter The Date:"))

print("The date you have entered is: %d-%s-%s"%(year,(str(month).zfill(2)) \
                                                ,(str(date).zfill(2))))

if  month in [1,3,5,7,8,10]:
    if date<31:
        date=int(str(date+1).zfill(2))
        month=int(str(month).zfill(2))     #add leading zeros
    else:
        date=int(str("1").zfill(2))
        month=int(str(month+1).zfill(2))
        
elif month in [4,6,9,11]:
    if date<30:
        date=int(str(date+1).zfill(2))
        month=int(str(month).zfill(2))
    else:
        date=int(str("1").zfill(2))
        month=int(str(month+1).zfill(2))
    
elif  month==2 :
    if (year%400==0 or  year%4==0) and date<29:
        date=int(str(date+1).zfill(2))
        month=int(str(month).zfill(2)) 
    elif(year%100!=0) and date<28:
        date=int(str(date+1).zfill(2))
        month=int(str(month).zfill(2))     
    else:
         date=int(str("1").zfill(2))
         month=int(str(month+1).zfill(2))
         
elif month==12:
    if date<31:
        date=int(str(date+1).zfill(2))
    else:
        date=int(str("1").zfill(2))
        month=int(str("1").zfill(2))
        year=year+1
        
print("The Next Date Is :%d-%s-%s"%(year,str(month).zfill(2),str(date).zfill(2)))
    
    