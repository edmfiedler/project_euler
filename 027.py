"""
Euler discovered the remarkable quadratic formula:
    n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39
 However, when
    n = 40, 40**2+40+41=40(40+1)+41
 is divisible by 41, and certainly when
    n = 41, 41**2+41+41
 is clearly divisible by 41.

The incredible formula n**2-79n+1601
 was discovered, which produces 80 primes for the consecutive values
 0 <= n <= 79
 The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
 n**2+an+b, where and |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""
import math

# Check if evaluation is prime
def remquadformula(n,a,b):
    y = (n**2)+a*n+b
    # Accept if == 2
    if y == 2:
        p = 1
    # Eliminate if negative or even
    elif (y < 2) or (y%2 == 0):
        p = 0
    # Check if the odd number is prime
    else:
        p = 1
        for x in range(2,int(math.sqrt(y)+1)):
            if (y%x == 0):
                p = 0
    return p

max_k = 0; max_a = 9999; max_b = 9999
# Generate the formulas
for a in range(-999,1000):
    for b in range(-999,1000):
        # Assume prime
        p = 1; n = 0; k = 0
        while p == 1:
            k += 1
            p = remquadformula(n,a,b)
            n += 1

        if k > max_k:
            print(k,max_a,max_b)
            max_k = k
            max_a = a
            max_b = b

print(max_a*max_b)