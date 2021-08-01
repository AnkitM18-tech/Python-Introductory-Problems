# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:15:41 2020

@author: OCAC
"""
widgetwgt=75
gizmoswgt=112
noWidget=int(input("Enter no of widgets:"))
noGizmos=int(input("Enter no of gizmos:"))

totalwgt=(widgetwgt*noWidget)+(gizmoswgt*noGizmos)

print("The Total Weight Of the order=",totalwgt,"grams")