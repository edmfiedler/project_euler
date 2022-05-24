"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
 it may incorrectly believe that 49/98 = 4/8, which is correct,
  is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
 less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
 find the value of the denominator.
"""
from fractions import Fraction

# Generate the 2 digit range
prod = 1
for a in range(10,100):
    for b in range(10,100):
        if (a/b > 1):
            continue

        a_str = str(a)
        b_str = str(b)
        if (len(a_str) > len(set(a_str))):
            continue

        i = 0
        for x in a_str:
            j = 0
            for y in b_str:
                if (x == y) and (i != j):
                    if int(b_str[::-1][j]) != 0:
                        canc_frac = int(a_str[::-1][i])/int(b_str[::-1][j])
                        if canc_frac == (a/b):
                            prod = prod*(a/b)
                            print(a,b,a/b,canc_frac)
                j += 1
            i += 1

print(Fraction(str(round(prod,5))))