# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:40:40 2020

@author: OCAC
"""
deposit_1ltr=0.10
deposit_morethan1ltr=0.25
container_upto1ltr=int(input("Enter The No Of Containers upto 1 Ltr:"))

container_morethan1ltr=int(input("Enter The No Of Containers more than 1 Ltr:"))
refund_for1ltr=deposit_1ltr*container_upto1ltr
refund_formorethan1ltr=deposit_morethan1ltr*container_morethan1ltr
refund=refund_for1ltr+refund_formorethan1ltr
print("The total refund after returning the container =$ %.2f."% refund)