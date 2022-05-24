"""
A permutation is an ordered arrangement of objects. For example,
 3124 is one possible permutation of the digits 1, 2, 3 and 4.
  If all of the permutations are listed numerically or alphabetically,
   we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
def permutations(dig_dat,i,digs_l):
    if (i == digs_l):
        perms.append(''.join(dig_dat))
    else:
        for j in range(i,digs_l):
            # Swap the entries
            dig_dat[i], dig_dat[j] = dig_dat[j], dig_dat[i]
            # With the fixed entry, swap the remaining entries
            permutations(dig_dat,i+1,digs_l)
            # Backtrack, swap back
            dig_dat[i], dig_dat[j] = dig_dat[j], dig_dat[i]


digs = "0123456789"
digs_l = len(digs)
dig_dat = list(digs)
perms = []
permutations(dig_dat,0,digs_l)
print(sorted(perms)[int(1e6-1)])