"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

How many, not necessarily distinct, values of n choose r for 1 <= n <= 100 are greater than 1 million?
"""
import math

k = 0
for n in range(1,101):
    for r in range(1,n+1):
        comb = int(math.factorial(n)/(math.factorial(r)*(math.factorial(n-r))))
        if comb > 1e6:
            k += 1

print(k)