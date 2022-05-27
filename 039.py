"""
If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

# a**2 + b**2 = c**2

list_sol = []
# Set range
a = 1; r = 1000
while a < r:
    b = 1
    # Allow b to only exist while it is smaller than a, this prevents double solutions e.g. (3,4,5) and (4,3,5)
    while b < r and b <= a:
        c = math.sqrt(a**2+b**2)
        if c - int(c) == 0:
            p = int(a+b+c)
            # Only solutions <= 1000 required
            if p <= 1000:
                list_sol.append(p)
        b += 1

    a += 1

# Obtain the item with maximum count in the list
print(max(list_sol, key = list_sol.count))