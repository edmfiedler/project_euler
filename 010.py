"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

num = int(2e6); sum = 2

# Find primes
for i in range(3,num,2):
    prime = 1 # Assume every number is prime
    for j in range(3,int(math.sqrt(i)+1),2): # Only need to do every 2
        if (i%j == 0):
            prime = 0 # If factor is found, not a prime, can break
            break

    if prime == 1:
        sum = sum + i

print(sum)