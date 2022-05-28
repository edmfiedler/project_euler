"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import math

primes = [2]
not_found = True
n = 3
# Add 1 to loop, determine if prime and add to list, then check the factors
founds = []
while not_found:
    prime = 1
    for x in range(2,int(math.sqrt(n))+1):
        if n % x == 0:
            prime = 0
            break
    if prime == 1:
        primes.append(n)
    # Check prime factors
    facs = []
    for y in primes:
        z = n
        while  z % y == 0:
            facs.append(y)
            z = z / y
    n_facs = len(set(facs))
    if n_facs == 4:
        founds.append(n)
        if len(founds) >= 2:
            if founds[-1] - founds[-2] == 1:
                if len(founds) == 4:
                    not_found = False
            else:
                # If reset, the last value in founds must become the only value for the next iteration
                founds = [founds[-1]]
    n += 1
# Program takes a while, because it is checking and saving primes. Instead, the factors could be searched of
# n from 2 to sqrt(n) to and numbers are checked then if prime
print(founds[0])