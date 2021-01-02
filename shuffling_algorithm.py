#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:04:48 2020

@author: baptistelafoux
"""

import domino 
import numpy as np
import numpy.lib.arraysetops as aso 

def spawn_block(x, y):

    if np.random.rand() > 0.5: 
        d1 = domino.domino(np.array([x,     y]), np.array([x + 1,     y]), np.array([0,-1]))
        d2 = domino.domino(np.array([x, y + 1]), np.array([x + 1, y + 1]), np.array([0, 1]))
    else: 
        d1 = domino.domino(np.array([x,     y]), np.array([x,     y + 1]), np.array([-1,0]))
        d2 = domino.domino(np.array([x + 1, y]), np.array([x + 1, y + 1]), np.array([ 1,0]))
    
    return [d1, d2]

def aztec_grid(order, only_new_blocks = True):

    grid_X, grid_Y = np.meshgrid(np.arange(2 * order) - (2 * order - 1)/2 , np.arange(2 * order) - (2 * order - 1)/2)
    
    center_pts = np.array([grid_X.flatten(), grid_Y.flatten()]).T
    center_pts = center_pts[np.lexsort((center_pts[:,1], center_pts[:,0]))]
    
    X = center_pts[:,0]
    Y = center_pts[:,1]
    if only_new_blocks: idx = (np.abs(X) + np.abs(Y) <= order) & (np.abs(X) + np.abs(Y) > order - 1)
    else: idx = np.abs(X) + np.abs(Y) <= order
    
    return X[idx], Y[idx]

def add_to_grid(tiles, grid): 
    
    for tile in tiles:
        grid[tile.pt1[0], tile.pt1[1]] = tile 
        grid[tile.pt2[0], tile.pt2[1]] = tile 
    
    return grid

def generate_good_block(grid):
    
    center_pts = np.array([*grid])
    center_pts = center_pts[np.lexsort((center_pts[:, 1], center_pts[:, 0]))]
    
    X = center_pts[:, 0]
    Y = center_pts[:, 1]
    
    for (x,y) in zip(X,Y):
        
        try:
            if ~grid[x, y]:
                idx = [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]
                try:
                    should_create_a_block = ~np.sum(np.array(list(map(grid.get, idx))), dtype = bool)
                    if should_create_a_block:
                        grid = add_to_grid(spawn_block(x, y), grid)
                except: pass
        except: pass
                    
    
    return grid
    

def enlarge_grid_deprec(grid, order):
    center_pts = [*grid]
    
    X_aztec, Y_aztec = aztec_grid(order)
    center_pts_aztec = [tuple([x,y]) for (x,y) in zip(X_aztec, Y_aztec)]
    
    diff_array = set(center_pts_aztec) - set(center_pts)

    if order > 1:
        for x, y in list(diff_array):
            grid[x, y] = False 
    else:
        for (x,y) in zip(X_aztec, Y_aztec): 
            grid[x, y] = False 


    return grid

def enlarge_grid(grid, order):
    
    X_aztec, Y_aztec = aztec_grid(order, True)
    
    for (x,y) in zip(X_aztec, Y_aztec): 
        grid[x, y] = False 

    return grid

def move_tiles(grid, curr_order): 
    temp_grid = {}
    for coord in grid:
        if grid[coord] != False:
            
            x1, y1 = grid[coord].pt1
            x2, y2 = grid[coord].pt2
            
            grid[coord].move()
            temp_grid = add_to_grid([grid[coord]], temp_grid)
            
            grid[x1, y1] = False
            grid[x2, y2] = False
        
    for coord in temp_grid:
        grid[coord] = temp_grid[coord]
                        
        
    return grid

def destroy_bad_blocks(grid):
    center_pts = np.array([*grid])
    
    X = center_pts[:, 0]
    Y = center_pts[:, 1]
    
    for (x,y) in zip(X,Y):
        try:
            next_x, next_y = np.array([x, y]) + grid[x, y].v
        
            if (grid[next_x, next_y] != False): 
                
                if all(grid[next_x, next_y].v == - grid[x, y].v): 
                
                    grid[x,      y     ] = False 
                    grid[next_x, next_y] = False
        except: pass
                
    return grid
    
    

