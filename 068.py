"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external
 node (4,3,2 in this example), each solution can be described uniquely. For example,
  the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
 the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
 What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

import itertools
from copy import deepcopy

size = 5

nums = [x for x in range(1,size*2+1)]
min = sum(nums[0:3])
max = sum(nums[-3:])+1

# Starting values
perm_start = list(itertools.permutations(nums,3))

def buildring(ring,n_used,des):
    possib = [deepcopy(ring)]
    n_use = [deepcopy(n_used)]
    for r in range(len(ring[1:])):
        n_u_buffer = []
        possib_buffer = []
        for k, rng in enumerate(possib):
            n_available = [n for n in range(1, size * 2 + 1) if n not in n_use[k]]
            if rng[r+1].count(0) == 2:
                p_n = list(itertools.permutations(n_available,2))
                for n in p_n:
                    if sum(n)+rng[r+1][1] == des and n[0] > ring[0][0]:
                        ring_curr = deepcopy(possib[k])
                        ring_curr[r+1][0] = n[0]
                        ring_curr[r+1][2] = n[1]
                        ring_curr[r+2][1] = n[1]
                        used = n_use[k]+[nums for nums in n]
                        n_u_buffer.append(used)
                        possib_buffer.append(deepcopy(ring_curr))
            if rng[r+1].count(0) == 1:
                if sum(rng[r+1]) + n_available[0] == des:
                    if n_available[0] > ring[0][0]:
                        ring_curr = deepcopy(possib[k])
                        ring_curr[-1][0] = n_available[0]
                        return ring_curr

            # Remove if no combination available
            if rng[r+1].count(0) > 0:
                continue
        possib = deepcopy(possib_buffer)
        n_use = deepcopy(n_u_buffer)
        if len(possib) < 1:
            return 0

rings = []
for x in range(min,max):
    for start in perm_start:
        if sum(start) == x:
            ring = [[0]*3 for k in range(size)]
            ring[0] = list(start)
            ring[1][1] = start[2]
            ring[-1][-1] = start[1]
            ring = buildring(ring,ring[0],x)
            if ring != 0:
                rings.append(ring)

ring_strings = []
for ring in rings:
    ring_string = ''
    for sec in ring:
        string_ring = [str(x) for x in sec]
        ring_string += ''.join(string_ring)
    if len(ring_string) == 16:
        ring_strings.append(int(ring_string))

print(sorted(ring_strings)[-1])