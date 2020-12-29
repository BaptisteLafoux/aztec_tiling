import numpy as np 
import random

from shapely.geometry import Point
from domino import domino 

import graphics 


def remove_bad_blocks(tiling):
    for tile in tiling:
        tile.move()
        
        colliding = np.argwhere(tiling == tile)
        if len(colliding) > 1:

            tiling = np.delete(tiling, colliding)
        else :
            tile.move(direct=-1)
        
    return tiling

def fill_blanks_with_blocks(tiling, order):
    
    X, Y = graphics.aztec_grid(order)
    
    pos = np.array([X, Y]).T
    pos = pos[np.lexsort((-Y, X))]
    
    X = pos[:,0].flatten()
    Y = pos[:,1].flatten()
        
    coverage = np.empty_like(X)
    
    for i, (x,y) in enumerate(zip(X, Y)):
        pt = Point(x,y)
        
        coverage[i] = False
        for tile in tiling: 
            if pt.within(tile.body):
                coverage[i] = True
    
    for i, occ in enumerate(coverage.astype(bool)):
        idx_adj = ((X == X[i]) &  (Y == Y[i] - 1)) + ((X == X[i] + 1) &  (Y == Y[i])) + ((X == X[i] + 1) &  (Y == Y[i] - 1))
        
        adj_are_empty = (np.sum(coverage[idx_adj]) == 0) & (len(coverage[idx_adj]) == 3)
        
        if ~occ & adj_are_empty: 
            
            d1, d2 = generate_random_block(X[i], Y[i])
            tiling = np.append(tiling, np.array([d1, d2]))
            coverage[i] = True
            coverage[idx_adj] = True 
            
    #print(np.sum(~coverage.astype(bool)))
            
    return tiling
            
def generate_random_block(x, y):
    if random.random() > 0.5: 
        d1 = domino(np.array([0, 1]), np.array([[x, y], [x + 1, y]]))
        d2 = domino(np.array([0,-1]), np.array([[x, y - 1], [x + 1, y - 1]]))  
    else: 
        d1 = domino(np.array([-1, 0]), np.array([[x, y], [x, y - 1]]))
        d2 = domino(np.array([ 1, 0]), np.array([[x + 1, y], [x + 1, y - 1]]))          
            
    return d1, d2 



def generate_aztec_tiling(tiling, target_order, curr_order=1): 
    if curr_order < target_order:
        
        tiling = remove_bad_blocks(tiling)
        
        for tile in tiling:
            tile.move()
        
        tiling = fill_blanks_with_blocks(tiling, curr_order + 1)
        
        print(curr_order/target_order)
        return generate_aztec_tiling(tiling, target_order, curr_order + 1)
                
    else:
        return tiling 