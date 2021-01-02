#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:16:34 2020

@author: baptistelafoux
"""
import matplotlib.pyplot as plt
import numpy as np 

import graphics

class domino: 
    def __init__(self, pt1, pt2, v):
        self.pt1 = pt1
        self.pt2 = pt2
        
        self.v = v
        if self.v[0] == 1: self.col = 'r'
        if self.v[0] ==-1: self.col = (1, 1, 0.2)
        if self.v[1] == 1: self.col = 'm'
        if self.v[1] ==-1: self.col = 'c'
    
    def move(self):
        self.pt1 += self.v
        self.pt2 += self.v
    
    def show(self):

        p1 = graphics.square(self.pt1)
        p2 = graphics.square(self.pt2)
        
        p = p1.union(p2)
        
        #plt.plot(*p.exterior.xy, 'k-')        
        plt.fill(*p.exterior.xy, color=self.col)

        


        
        
        
        
        
        
        
        
        
        