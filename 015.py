"""
Starting in the top left corner of a 2×2 grid,
 and only being able to move to the right and down,
  there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Can only move left and down
# To get to the goal, must always move grid size down, grid size right

# How many combinations are there for this operation?

# r r d d
# r d r d
# r d d r
# d r r d
# d r d r
# d d r r

# Moves are mirrored

import numpy as np

# Generate the grid
size_grid = 20
lat = np.zeros((size_grid+1,size_grid+1))
lat[0,0] = 1; lat[size_grid,size_grid] = 1; lat[0,1] = 1

# Start initial position as if first move is right
pos = [(0,1,1)]
for i in range(size_grid*2-2):
    npos = []
    for j in pos:
        # Check moves down and right are possible
        if (j[0]+1<=size_grid and j[1]+1<=size_grid):
            npos.append((j[0]+1,j[1],j[2]))
            npos.append((j[0],j[1]+1,j[2]))

        # Check if move can only be to the right
        if (j[0]+1>size_grid):
            npos.append((j[0],j[1]+1,j[2]))

        # Check if move can only be down
        if (j[1] + 1 > size_grid):
            npos.append((j[0]+1, j[1],j[2]))

    # Check for duplicate positions
    for k in range(len(npos)-1):
        for l in range(k+1,len(npos)):
            if (npos[k] == npos[l]) and (npos[k] != 0):
                # Sum the paths from the duplicate position as path is unique
                npos[k] = (npos[k][0],npos[k][1],npos[k][2]+npos[l][2])
                npos[l] = 0

    # Remove the redundant items to save storage
    nlist = []
    for k in npos:
        if k != 0:
            nlist.append(k)

    # Update path positions
    pos = nlist

# Sum number of paths
sum_paths = 0
for p in pos:
    sum_paths = sum_paths + p[2]

# Multiply paths * 2 as first move assumed was to the right
print(sum_paths*2)