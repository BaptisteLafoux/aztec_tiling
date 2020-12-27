#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:45:05 2020

@author: baptistelafoux
"""

import matplotlib.pyplot as plt
import numpy as np 
from shapely.geometry import Polygon
from shapely.affinity import translate

def centered_sqr(pos):
    x = pos[0]
    y = pos[1]
    p = Polygon([(x - 1/2, y - 1/2),
                 (x + 1/2, y - 1/2),
                 (x + 1/2, y + 1/2),
                 (x - 1/2, y + 1/2)])
    return p 

class domino:
    def __init__(self, v = np.zeros(2), pos_ini = np.array([[0.5, 0.5], [0.5, 1.5]])):
        self.v = v
        
        s1 = centered_sqr(pos_ini[0,:])
        s2 = centered_sqr(pos_ini[1,:])
        self.shape = s1.union(s2)
    
    def move(self):
        self.shape = translate(self.shape, self.v[0], self.v[1], 0)
    
    def draw(self):
        plt.fill(*self.shape.exterior.xy, color='r', alpha=1)




def draw_sqr(x, y, color=None, alpha=0.9) : 

    p = centered_sqr([x, y])
    plt.plot(*p.exterior.xy, 'k-')       
    plt.fill(*p.exterior.xy, color=color, alpha=alpha)
    
            
def draw_grid(X, Y):

    for (x,y) in zip(X.flatten(), Y.flatten()):    
        if (x + y) % 2 == 0: alpha = 0 
        draw_sqr(x, y, 'k', alpha)
        
            
def grid(n): 
    
    x, y = np.arange(n) - (n - 1)/2 , np.arange(n) - (n - 1)/2
    X, Y = np.meshgrid(x, y)
    return X, Y 
        
def aztec_grid(order):
    
    X, Y = grid(2 * order)
    idx = np.abs(X) + np.abs(Y) <= order
    return X[idx], Y[idx]
    

# def generate_aztec_tiling(order): 
#     if order > 0:
        
#     else:
#         return tiling 

plt.close('all')   
o = 2

plt.figure(0)
X, Y = aztec_grid(o)

plt.plot(X, Y, 'k.')
draw_grid(X, Y)

d1 = domino()
d1.draw()
d1.v = np.array([-1, 0])
d1.move()
d1.draw()
# p = Polygon([(0, 0),
#              (2, 0),
#              (2, 1),
#              (0, 1)])

# p2 = translate(p, 0, -1, 0)
# plt.fill(*p.exterior.xy,  'r-', alpha=1)
# plt.fill(*p2.exterior.xy, 'g-', alpha=1)

plt.axis('scaled')
plt.axis('off')


