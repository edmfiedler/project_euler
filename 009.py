"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

# Define function for finding the triplet
def pyTriplet():
    for a in range(1,500):              # Set range 1 to 500 because a + b + c == 1000
        for b in range(1,500):          # Set same range
            c = math.sqrt(a**2+b**2)    # Obtain Pythagorean
            # Check if triplet
            if (c%int(c) == 0):
                if (a+b+c == 1000):
                    return a, b, int(c) # Break if the triplet has been found

a,b,c = pyTriplet()
print(math.prod([a,b,c]))