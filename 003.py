"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

num = 600851475143
for i in range(3,int(math.sqrt(num)+1),2):  # Set up range from 3 up to highest possible factor
    p_cond = 1
    for j in range(2,int(math.sqrt(i))+1):  # Range to check if prime
        # Identify if not prime
        if (i%j == 0):
            p_cond = 0
            break

    # Condition if prime and multiple, overwrite value
    if p_cond == 1:
        if (num%i == 0):
            prime = i

print(prime)