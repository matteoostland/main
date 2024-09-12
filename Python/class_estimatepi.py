# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:14:36 2024

@author: tomke
"""
k=100
tot=0
for j in range(k):
    tot += 4*(-1)**j * 1/(2*j+1)
print(tot)