# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:00:43 2016

@author: Matthew
"""

import numpy as np

G = 6.67408e-11
mSun = 1.9891e30

def initSun():
    return ["Sun", mSun, 0, 0, 0, 0, 0, 0]
    
def initBody(name, mass, a, e):
    x = a*(1+e)
    y = 0
    z = 0
    vx = 0
    vy = np.sqrt((1-e)/(1+e))*np.sqrt((mSun*G)/a)
    vz = 0
    return [name, mass, x, y, z, vx, vy, vz]
    
def distanceTo(tempCoords, body2):
    distx = tempCoords[0] - body2[2]
    disty = tempCoords[1] - body2[3]
    distz = tempCoords[2] - body2[4]
    return np.sqrt(np.power(distx, 2) + np.power(disty, 2) + np.power(distz, 2))