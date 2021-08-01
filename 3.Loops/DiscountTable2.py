# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:09:00 2020

@author: OCAC
"""

price=4.95
discount=0.6
print("Original Price\t\tDiscount Price\t\tPurchase Price")
for i in range(5):
    discountPrice=price*discount
    purchasingPrice=price-discountPrice
    print("%.2f\t\t\t%.2f\t\t\t%.2f"%(price,discountPrice,purchasingPrice))
    price+=5