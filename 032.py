"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
 for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
 containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# Generate combinations of multipliers
products = []
for x in range(1,9999):
    if len(set(str(x))) < len(str(x)):
        continue
    for y in range(1,9999):
        if len(set(str(y))) < len(str(y)):
            continue

        z = x*y
        st = str(x) + str(y) + str(z)
        if (len(st) > 9):
            break

        if (len(st) == 9) and (len(set(st)) == len(st)) and '0' not in st:
            products.append(z)

products = set(products)
print(sum(products))