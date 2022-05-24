"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math

# Find primes below one million
primes = [2]
for n in range(3,int(1e6),2):
    prime = 1
    for m in range(2,int(math.sqrt(n)+1)):
        if n % m == 0:
            prime = 0
            break

    if prime == 1:
        primes.append(n)

circ_prime = []
for p in primes:
    p_s = str(p)
    circ_buff = []
    for i in range(len(p_s)):
        p_s = p_s[1:] + p_s[0]
        circ_buff.append(int(p_s))

    n_c = 0
    for j in circ_buff:
        if j not in primes:
            n_c = 1

    if n_c == 0:
        circ_prime.append(p)

print(len(circ_prime))