"""
This is a domino class used for aztec diamond grid tiling

A domino is a 2x1 or 1x2 rectangle embodied by a Polygon from shapely module 
Its characteristics are:
    - a body (Polygon, "body")
    - an orientation (N,E,S,W) (2x2 vector, "v")
    - a position (7x2 vector, "body.exterior.xy")
"""

import numpy as np 
import matplotlib.pyplot as plt

from shapely.affinity import translate

import graphics 

class domino:
    def __init__(self, v = np.zeros(2), pos_ini = np.array([[0.5, 0.5], [0.5, 1.5]])):
        self.v = v
        
        s1 = graphics.centered_sqr(pos_ini[0,:])
        s2 = graphics.centered_sqr(pos_ini[1,:])
        self.body = s1.union(s2)
        
    def __eq__(self, other): 
        return self.body.exterior.xy == other.body.exterior.xy
    
    def move(self, direct=1):
        self.body = translate(self.body, direct * self.v[0], direct * self.v[1], 0)
    
    def draw(self, col_border='k'):
        if self.v[0] == 1: col = 'b'
        if self.v[0] ==-1: col = 'r'
        if self.v[1] == 1: col = 'g'
        if self.v[1] ==-1: col = (1, 1, 0.2)
        
        plt.plot(*self.body.exterior.xy, col_border + '-', linewidth=1.5)
        plt.fill(*self.body.exterior.xy, color=col)

