# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:07:35 2020

@author: OCAC
"""
sec2day=86400
sec2min=60
sec2hour=3600
Sec=int(input("Enter The No of seconds:"))

print("The No of days is %.2d"%(Sec/sec2day))
Sec=Sec%sec2day

print("The No of hours is %.2d"%(Sec/sec2hour))
Sec=Sec%sec2hour

print("The No of minutes is %.2d"%(Sec/sec2min))
Sec=Sec%sec2min

print("The No of seconds is %.2d"%(Sec))

