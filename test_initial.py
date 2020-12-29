#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:45:05 2020

@author: baptistelafoux
"""
import matplotlib.pyplot as plt
import numpy as np 

import shuffling

plt.close('all')   
plt.figure()

order = 20

# initilization with a random order 1 tiling (2x2)
d1, d2 = shuffling.generate_random_block(-0.5, 0.5)       
tiling = np.array([d1, d2])

# tiling generation from recursive random shuffling algorithm 
tiling = shuffling.generate_aztec_tiling(tiling, order)

# graphic display of tiling 
for tile in tiling: 
    tile.draw()
    
plt.axis('scaled')
plt.axis('off')


