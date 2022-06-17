"""
Period square roots.

A square root can be represented as a series of divisions where an integer is added to a fraction etc.

For irrational square roots, the integer being added will be cyclical in that there is a repeating order of numbers required infinitely to express the root in this manner.

Find the number of odd period lengths for N <= 10,000
"""

o_count = 0
for n in range(1,10000+1):
    sq = n**0.5
    # Check if rational
    if int(sq)/sq == 1:
        continue
    # Build sequence
    not_found = True
    x = sq
    x_prev = sq
    k = 1
    while not_found:
        y = x - int(x)
        x = y**-1
        if k == 1:
            first = round(x,3)
        elif round(x,3) == first:
            if (k-1) % 2 == 1:
                o_count += 1
            #print(n,k-1)
            not_found = False
        k += 1
print(o_count)
