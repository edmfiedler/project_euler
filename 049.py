"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
 is unusual in two ways: (i) each of the three terms are prime, and,
  (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
 exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import math
from itertools import permutations

# Identify prime numbers between 1000 and 9999
primes = []
for x in range(1001,10000,2):
    prime = 1
    for y in range(2,int(math.sqrt(x))+1):
        if x % y == 0:
            prime = 0
            break

    if prime == 1:
        primes.append(x)

for x in primes:
    perms = list(set([int(''.join(p)) for p in permutations(str(x))]))
    p_perms = []
    for y in perms:
        if y in primes:
            p_perms.append(y)

    diffs = []
    for y in p_perms:
        diffs.append(abs(x-y))

    if len(set(diffs)) != len(diffs):
        comms = sorted(diffs, key = diffs.count)
        mc = comms[-1]
        for z in diffs:
            idx1 = diffs.index(mc)
            idx2 = diffs.index(mc,idx1+1)

        print(p_perms[idx1],x,p_perms[idx2])
