"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

l10_sum = "0000000000"
n_digs = 10
for i in range(1,1001):
    # Loop by number of i
    prod = 1
    for x in range(1,i+1):
        prod *= i
        sprod = str(prod)
        if len(sprod) >= n_digs:
            prod = int(sprod[-n_digs::])
    l10_sum = str(int(l10_sum) + prod)
print(l10_sum[-10::])