"""
The number 3797 has an interesting property. Being prime itself,
 it is possible to continuously remove digits from left to right,
  and remain prime at each stage: 3797, 797, 97, and 7.
   Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math

def checktruncatable(n,primes,rev):
    truncable = 1
    for x in range(len(n)):
        strip = n[x::]
        if int(strip) not in primes and rev == 0:
            truncable = 0
            break

        if int(strip[::-1]) not in primes and rev == 1:
            truncable = 0
            break

    return truncable


# Find primes below one million
primes = [2]; ntrunc = 0; n = 3; strunc = 0
while ntrunc < 11:
    prime = 1
    for m in range(2,int(math.sqrt(n)+1)):
        if n % m == 0:
            prime = 0
            break

    if prime == 1:
        primes.append(n)
        if n > 7:
            ct1 = checktruncatable(str(n),primes,0)
            ct2 = checktruncatable(str(n)[::-1],primes,1)
            if ct1 + ct2 == 2:
                strunc += n
                ntrunc += 1

    n += 2

print(strunc)
