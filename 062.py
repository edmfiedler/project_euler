"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

perms = [1]
cubes = ['1']

not_found = True
n = 2
while not_found:
    cub = n**3
    digits = []
    digits[:0] = str(cub)
    digits = sorted(list(set(digits)))
    counts = [str(cub).count(d) for d in digits]
    for k, c in enumerate(cubes[::-1]):
        c_digits = []
        c_digits[:0] = c
        c_digits = sorted(list(set(digits)))
        c_counts = [c.count(d) for d in c_digits]
        if c_digits == digits and c_counts == counts:
            perms.append(perms[len(perms)-k-1]+[cub])
            if len(perms[-1]) == 5:
                print(len(perms[-1]),perms[-1])
                not_found = False
            break
        if len(str(cub)) > len(c):
            perms.append([cub])
            break
        if k-len(perms) == 0:
            perms.append([cub])
    cubes.append(str(cub))
    n += 1
