"""
It was proposed by Christian Goldbach that every odd composite number
 can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

# Go through odd numbers
# Check if prime

i = 9
primes = [2,3,5,7]
not_found = True
while not_found:
    prime = 1
    for x in range(2,int(math.sqrt(i))+1):
        if i % x == 0:
            prime = 0
            break
    if prime == 1:
        primes.append(i)
    if prime == 0:
        for y in range(len(primes)-1,-1,-1):
            n = 1
            while primes[y] + 2*n**2 < i:
                n += 1
            if primes[y] + 2*n**2 == i:
                break
            if y == 0 and primes[y] + 2*n**2 != i:
                not_found = False
    i += 2
print(i)