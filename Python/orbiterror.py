# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 07:44:21 2024

@author: Robert Santmann
"""

#orbitDays = float(input('Orbit days?))


import numpy as np
orbitMinutes = np.array([94., 4*60., 6*60., 773.])

T = orbitMinutes*60
G = 6.67430*10**-11
Me = 5.97219*10**24
pi = 3.14159265358
rE = 6378137

r = (((T**2)*G*Me)/(4*pi**2))**(1/3)


h = r - rE
hkm = h/1000

print(hkm , "km")