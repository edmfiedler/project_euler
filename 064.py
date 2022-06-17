"""
Period square roots.

A square root can be represented as a series of divisions where an integer is added to a fraction etc.

For irrational square roots, the integer being added will be cyclical in that there is a repeating order of numbers required infinitely to express the root in this manner.

Find the number of odd period lengths for N <= 10,000
"""

o_count = 0
for n in range(1,10000+1):
    sq = n**0.5
    if int(sq)/sq == 1:
        continue
    a = int(sq)
    m = 0
    d = 1
    
    count = 0
    while int(sq)*2 != a:
        m = d*a-m
        d = (n-m**2)/d
        a = int((int(sq)+m)/d)
        count += 1
    if count % 2 == 1:
        o_count += 1
print(o_count)
