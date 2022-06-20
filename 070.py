"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to 
nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio 
n/φ(n) produces a minimum.
"""

max_n = 10**7
p = [2]
for n in range(3,max_n):
    prime = 1
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            prime = 0
            break
    
    if prime == 1:
        p.append(n)
print("-----")

min_t = 100
# Relative primes
for n in range(2,max_n):
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
    
    list_n = sorted(list(set(str(n))))
    count_n = [str(n).count(x) for x in list_n]
    
    list_phi = sorted(list(set(str(phi))))
    count_phi = [str(phi).count(x) for x in list_phi]
    
    if list_n == list_phi and count_n == count_phi:
        if tot < min_t:
            min_t = tot
            n_min = n
            print(phi,n)
