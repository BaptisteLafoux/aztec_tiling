#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:20:17 2020

@author: baptistelafoux
"""

import shuffling_algorithm as sa

import matplotlib.pyplot as plt
import numpy as np 


grid = {}

target_order = 75
curr_order = 1 

while curr_order < target_order: 
    grid = sa.enlarge_grid(grid, curr_order)
    grid = sa.move_tiles(grid, curr_order)
    grid = sa.generate_good_block(grid)
    
    grid = sa.destroy_bad_blocks(grid)
    curr_order += 1
    print(curr_order)

sa.generate_good_block(grid)

plt.close('all') 
plt.figure()

for coord in grid:
    if grid[coord] != False:
        grid[coord].show()     

t = np.linspace(0, 2*np.pi, 200)
R = (curr_order) * np.sqrt(2) / 2
plt.plot(R * np.cos(t), R * np.sin(t), 'w-', linewidth=3)

plt.axis('scaled')
plt.axis('off')

plt.savefig('tiling_order%i'%curr_order + '.pdf')


