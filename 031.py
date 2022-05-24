"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import numpy as np

# Coin types available
coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]
# Iterations up to 2
denom = [x/100 for x in range(201)]

# Generate table
tab = np.zeros((len(coins)+1,len(denom)+1))
tab[0,1::] = denom
tab[1::,0] = coins
tab[1::,1] = 1
tab[1,2::] = 1

# If a coin value is above the iteration, it copies the value above
# Otherwise, take the difference, and find this value in denom corresponding to coin
# The amount of variations will be at the bottom right of the table
pos = (2,2); c = 0
for coin in coins[1::]:
    pos = (2+c,2)
    for i in range(len(denom[1::])):
        c_s = (0,pos[1])
        c_up = (pos[0] - 1, pos[1])
        if tab[c_s] < coin:
            tab[pos] = tab[c_up]
        else:
            d = round(tab[c_s]-coin,2)
            tab[pos] = tab[c_up] + tab[pos[0],denom.index(d)+1]

        pos = (pos[0],3+i)

    c += 1

print(tab[-1,-1])