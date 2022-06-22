"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

D = 12000
fracts = []

for d in range(2,D+1):
    sieve = [0,1]+[1]*(d-2)
    for k, s in enumerate(sieve):
        if k < 2:
            continue
        else:
            if d % k == 0:
                sieve[k::k] = [0]*len(sieve[k::k])
    for k, s in enumerate(sieve):
        if s == 1:
            fracts.append(k/d)

fracts = sorted(fracts)
idx_1 = fracts.index(1/3)
idx_2 = fracts.index(1/2)
print(idx_2-idx_1-1)