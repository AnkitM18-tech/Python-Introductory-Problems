# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:49:45 2020

@author: OCAC
"""

discount=0.6
original_prices=[4.95,9.95,14.95,19.95,24.95]

for i in range(5):
    discountPrice=original_prices[i]*discount
    newPrice=original_prices[i]-discountPrice
    print("The Original Price Of No.%d item is :     %.2f"%(i+1,original_prices[i]))
    print("The Discounted Price is :                %.2f"%discountPrice)
    print("The New Price For purchase is :          %.2f\n"%newPrice)
    

