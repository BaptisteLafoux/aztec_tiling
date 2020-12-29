#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:41:43 2020

@author: baptistelafoux

Graphical and geometrical functions used for tiling algorithm of aztec diamond grids 
"""

import numpy as np 
import matplotlib.pyplot as plt

from shapely.geometry import Polygon

def centered_sqr(pos):
    x = pos[0]
    y = pos[1]
    p = Polygon([(x - 1/2, y - 1/2),
                 (x + 1/2, y - 1/2),
                 (x + 1/2, y + 1/2),
                 (x - 1/2, y + 1/2)])
    return p 

def draw_sqr(x, y, col='k', a=1) : 
    p = centered_sqr([x, y])
    plt.plot(*p.exterior.xy, col + '-', alpha=a)       
    
            
def draw_grid(X, Y):
    for (x,y) in zip(X.flatten(), Y.flatten()):    
        draw_sqr(x, y)
        
            
def grid(n): 
    x, y = np.arange(n) - (n - 1)/2 , np.arange(n) - (n - 1)/2
    X, Y = np.meshgrid(x, y)
    return X, Y 
        
def aztec_grid(order): 
    X, Y = grid(2 * order)
    idx = np.abs(X) + np.abs(Y) <= order
    return X[idx], Y[idx]