#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:58:52 2020

@author: baptistelafoux
"""
from shapely.geometry import Polygon

def square(pt): 
    
    center_x, center_y = pt
    
    s = Polygon([(center_x - 1/2, center_y - 1/2),
                 (center_x + 1/2, center_y - 1/2),
                 (center_x + 1/2, center_y + 1/2),
                 (center_x - 1/2, center_y + 1/2)])
    
    return s 


