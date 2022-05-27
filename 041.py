"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools
import math

# Generate primes, check if pandigital up to largest 9 digit pandigital
n = 2500

# Generate pandigital numbers, check if prime
for x in range(2,10):
    pan = ""
    for y in range(1,x+1):
        pan += str(y)

    a = itertools.permutations(pan)
    j = [''.join(i) for i in a]
    for z in j:
        z = int(z)
        if z % 2 == 0:
            continue
        prime = 1
        for k in range(2,int(math.sqrt(z))+1):
            if z % k == 0:
                prime = 0
                break

        if prime == 1:
            pan_prime = z

# Already sorted
print(pan_prime)