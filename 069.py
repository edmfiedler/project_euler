"""
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are 
all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

# Generate primes under 1000000
p = [2]
for n in range(3,1000000+1):
    prime = 1
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            prime = 0
            break
    
    if prime == 1:
        p.append(n)

max_t = 0
# Relative primes
for n in range(2,100):
    p_facs = []
    for f in p:
        if n % f == 0:
            p_facs.append(f)
        if f > n:
            break
    prod = 1
    for pf in p_facs:
        prod *= 1-(1/pf)
    
    phi = int(n*prod)
    tot = n/phi
    if tot > max_t:
        max_t = tot
        n_max = n
        print(n_max,max_t)
