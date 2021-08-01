# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:33:21 2020

@author: OCAC
"""
Aplus=4.0
Aminus=3.7
Bplus=3.3
B=3.0
Bminus=2.7
Cplus=2.3
C=2.0
Cminus=1.7
Dplus=1.3
D=1.0
F=0
CGP=0
grade=input("Enter The Grade(blank to quit):")
i=0
  
while grade!="":
    if grade=="A+" or grade=="A":
        points=Aplus
    elif grade=="A-":
        points=Aminus
    elif grade=="B+":
        points=Bplus
    elif grade=="B":
        points=B
    elif grade=="B-":
        points=Bminus
    elif grade=="C+":
        points=Cplus
    elif grade=="C":
        points=C
    elif grade=="C-":
        points=Cminus
    elif grade=="D+":
        points=Dplus
    elif grade=="D":
        points=D
    else:
        points=F
        
    CGP+=points
    i+=1
    grade=input("Enter The Grade(blank to quit):")
    
CGPA=CGP/i

print("The Grade Point Average is :",CGPA)
    