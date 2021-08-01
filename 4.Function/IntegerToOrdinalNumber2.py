# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 03:13:25 2020

@author: OCAC
"""
def ItO(num):
     num_dict={1:"First",2:"Second",3:"Third",4:"Fourth",5:"Fifth",6:"Sixth",7:"Seventh",8:"Eighth",
              9:"Nineth",10:"Tenth",11:"Eleventh",12:"Twelveth"}
     
     if num in num_dict:
         return num_dict[num]
     else:
         return " "
     
if __name__ == '__main__':
   num=int(input("Enter A Number:"))
   ordinal=ItO(num) 
   print("The Ordinal Value of the Num is:",ordinal)     
        
        
   

     
