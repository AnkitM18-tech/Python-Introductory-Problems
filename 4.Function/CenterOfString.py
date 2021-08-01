# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:50:19 2020

@author: OCAC
"""
WIDTH=80

def stringCenter(line,width):
    if width<len(line):
        result=line
        
    spaces=(width-len(line))//2
    result=" "*spaces+line
    
    return result

if __name__=='__main__':
    print(stringCenter("A Famous Story",WIDTH))
    print(stringCenter("by:",WIDTH))
    print(stringCenter("Someone Famous",WIDTH))
    print()
    print("Once Upon a Time...")
    
