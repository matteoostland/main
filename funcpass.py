# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:48:57 2018

@author: Tom K
"""
import numpy as np

def fpass(func,a,b):
    return func(a) - func(b)

def feven(ilist):
   a = list(filter(lambda x: x%2==0,ilist))
   print(a)
   return a

def fmap(func,ilist):
    a=list(map(func,ilist))
    print(a)
    return(a)
    
def fmany(*args):
    m = 0
    for arg in args:
        m +=arg
    return m

def fdict(**junk):
    #you will often see the input written as **kwargs
    for key, values in junk.items():
        print(key,'=', values)
        
    
        
        
        