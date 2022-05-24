"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import numpy as np

size = 1001+2
map = np.zeros((size,size))
center = (int(size/2),int(size/2))
map[center[0],center[1]] = 1
map[center[0],center[1]+1] = 2

# Current location
loc = (center[0],center[1]+1)
for x in range(3,(size-2)**2+1):
    check = loc
    c_up = (check[0]-1,check[1])
    c_do = (check[0]+1,check[1])
    c_le = (check[0],check[1]-1)
    c_ri = (check[0],check[1]+1)

    if (map[c_le] != 0) and (map[c_do] == 0):
        loc = c_do
        map[c_do] = x
        continue

    if (map[c_up] != 0) and (map[c_le] == 0):
        loc = c_le
        map[c_le] = x

    if (map[c_ri] != 0) and (map[c_up] == 0):
        loc = c_up
        map[c_up] = x

    if (map[c_ri] == 0) and (map[c_do] != 0):
        loc = c_ri
        map[c_ri] = x

map = map[1:size-1,1:size-1]
print(np.trace(map)+np.trace(np.fliplr(map))-1)