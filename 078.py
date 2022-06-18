"""
Let p(n) represent the number of different ways in which n coins can be separated into piles.
 For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO    O
OOO     OO
OOO     O   O
OO      OO  O
OO      O   O   O
O       O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+...
# An alternating sum of pentagonal numbers

pents = [1]
p_n = -1
p = [1, 1, 2, 3]
coins = 4
while p[-1] % int(1e6) != 0:
    # Generate pentagonal numbers if necessary
    while pents[-1] < coins:
        pents.append(int((3*p_n**2-p_n)/2))
        if p_n < 0:
            p_n = abs(p_n) + 1
        else:
            p_n = -p_n
    # Generate the alternating sum
    perms = 0
    constituents = []
    for x in pents:
        if coins-x >= 0:
            constituents.append(coins-x)
        else:
            break

    np = 0
    for k, x in enumerate(constituents):
        # Check if even
        if k % 2 == 0:
            if int(k/2) % 2 == 0:
                perms += p[x]
                np = 1
            else:
                perms -= p[x]
                np = 0
        elif np == 1:
            perms += p[x]
        elif np == 0:
            perms -= p[x]

    p.append(perms)
    coins += 1
print(coins-1)
