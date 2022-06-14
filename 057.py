"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

# sqrt(2) = 1 + 1/(2+(1/(2+(1/2+...

n_moredigits = 0
den = 2
n = 1
for x in range(999):
    nom = 1*den
    den = 2*den+n
    n = nom
    if len(str(nom+den)) > len(str(den)):
        n_moredigits += 1

print(n_moredigits)