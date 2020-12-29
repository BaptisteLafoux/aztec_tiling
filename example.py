import matplotlib.pyplot as plt
import numpy as np 

import shuffling

plt.close('all')   

# order of the aztec diamond 
order = 22

# initilization with a random order 1 tiling (2x2)
d1, d2 = shuffling.generate_random_block(-0.5, 0.5)       
tiling = np.array([d1, d2])

# tiling generation from recursive random shuffling algorithm 
tiling = shuffling.generate_aztec_tiling(tiling, order)

# graphic display of tiling 
plt.figure('Tiling of aztec diamond of order %i'%order)

for tile in tiling: 
    tile.draw()
    
plt.axis('scaled')
plt.axis('off')

plt.savefig('aztec_diamond_domino_tiling_order%i'%order + '.png')


