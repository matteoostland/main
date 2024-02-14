# -*- coding: utf-8 -*-
"""
@author: Tom
"""

import math as mh

def rising1D(v0,g=9.8):
    '''
    Parameters
    ----------
    v0 : float
        initial velocity of object fired up.
    g : float
        acceleration due to gravity. The default is 9.8.

    Returns
    -------
    h : float
        Maximum height of object.
    t : float
        time in the air.

    '''
    h = v0**2/(2*g)
    t = v0/g
    return h,t

def falling1D(h,v0=0):
    # returns the time and velocity of an object falling from h and at an initial velocity v0
    g=9.8
    #solution to quadratic equation
    time = -v0/g + mh.sqrt(v0**2/g**2+2*h/g)
    velo = mh.sqrt(v0**2+2*g*h)
    return time,velo

def projectile(v0, angle, h):
    # return time and rang
    deg2rad = lambda ang: ang*mh.pi/180
    angle = deg2rad(angle)
    #component breakdown
    vx = v0*mh.cos(angle)
    vy0 = v0*mh.sin(angle)
    [maxh, t1] = rising1D(vy0)
    [t2, vf] = falling1D(maxh)
    # add both times
    time = t1+t2
    rang = vx * time
    return time, rang

if __name__ == '__main__':
    [t,rang] = projectile(54, 40, 40)
    print(f'This projectile travels {round(rang)} m in {round(t,2)} seconds')




