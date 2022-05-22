"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math

i = 2; no_prime = 1
while True:
    i = i + 1
    prime = 1
    # Check if the number is prime
    for j in range(2,int(math.sqrt(i)+1)):
       if (i%j == 0):
           prime = 0
           break

    # If prime, add it to the number of primes
    if prime == 1:
        no_prime = no_prime + 1

    # Break loop if the 10001th prime was found
    if no_prime == 10001:
        break

print(i)