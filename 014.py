"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def evCollatz(n):
    c = 1
    while (n != 1):
        c = c + 1
        if (n%2 == 0):
            n = n/2
        else:
            n = 3*n + 1

    return c

start = 0; max_collatz = 0
while start < 1e6:
    start = start + 1
    collatz = evCollatz(start)
    if collatz > max_collatz:
        max_collatz = collatz
        max_num = start

print(max_num)