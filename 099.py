"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math

with open('txt_files/p099_base_exp.txt') as f:
    lines = f.readlines()

BE = []
for k, l in enumerate(lines):
    if k < len(lines)-1:
        idx = l.index(',')
        BE.append((l[0:idx],l[idx+1:-1]))
    else:
        idx = l.index(',')
        BE.append((l[0:idx],l[idx+1:]))

max_v = 0
for k, p in enumerate(BE):
    b = int(p[0])
    e = int(p[1])
    bin_e = bin(e)[3:]
    # Simply compare exponent*log(base)
    B = e*math.log(b)
    if B > max_v:
        max_v = B
        max_k = k + 1
print(max_k)