"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import math

primes = [2]
for x in range(3,int(1e6),2):
    prime = 1
    for y in range(2,int(math.sqrt(x)+1)):
        if x % y == 0:
            prime = 0
            break
    if prime == 1:
        primes.append(x)

p_c = 1
n_c = 2
for k, p in enumerate(primes[2::]):
    prev_primes = primes[0:k+2]
    # Consecutive prime sums, only need to search for a consecutive length longer than longest and update this variable
    for l in range(n_c,len(prev_primes)+1):
        i = 0
        ex_cond = 0
        for c in range(len(prev_primes)-l+1):
            l_prev = prev_primes[c:c + l]
            c_sum = sum(l_prev)
            if c_sum > p and i == 0:
                ex_cond = 1
            else:
                i += 1
            if c_sum > p:
                break
            if c_sum == p:
                # Last entry will be the largest
                if len(l_prev) > n_c:
                    p_c = p
                    n_c = len(l_prev)
        if ex_cond == 1:
            break
print(p_c, n_c)
