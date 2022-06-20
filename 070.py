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

min_t = 100
n_max = 10000000
for n in range(n_max,3,-1):
    org = n
    phi = n
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            while n % x == 0:
                n /= x
            phi -= phi / x

    if n > 1:
        phi -= phi / n

    phi = int(phi)
    tot = org/phi
    list_n = sorted([x for x in str(org)])
    list_phi = sorted([x for x in str(phi)])

    if list_n == list_phi:
        if tot < min_t:
            min_t = tot
            n_min = org
            print(org,phi,tot)
print(n_min)
