"""
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 26972593ā1; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2pā1, have been found which contain
more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433Ć27830457+1.

Find the last ten digits of this prime number.
"""

prod = 28433
for n in range(1,7830457+1):
    prod *= 2
    # Take the last 10 digits if larger
    if len(str(prod)) > 10:
        prod = int(str(prod)[-10:])
        
print(prod+1)
