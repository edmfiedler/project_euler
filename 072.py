"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

D = 1000000
N = 0

# Build sieve up to 1000000
sieve = [0,0] + [1]*(D)
for k, s in enumerate(sieve):
    if k > int(D**0.5+1):
        break
    if s == 1:
        sieve[k * k::k] = [0] * len(sieve[k * k::k])

for d in range(2,D+1):
    S = sieve[0:int(d**0.5)+1]
    phi = d
    if sieve[d] != 1:
        facs = []
        for c, s in enumerate(S):
            if s == 1 and d % c == 0:
                facs.append(c)
        div = d
        all_facs = facs[:]
        for f in facs:
            while div % f == 0:
                div = int(div/f)
                if sieve[div] == 1 and div not in all_facs:
                    all_facs.append(div)
        for a in all_facs:
            phi *= 1-(1/a)
    else:
        phi -= 1


    phi = int(phi)
    N += phi

print(N)