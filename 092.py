"""
A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

n_max = 10000000
e_n = 0
for n in range(1,n_max):
    n_str = str(n)
    s = n
    while s != 1 and s != 89:
        s = 0
        for i in n_str:
            s += int(i)**2
        n_str = str(s)
    if s == 89:
        e_n += 1
print(e_n)
