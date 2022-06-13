"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

k = 1
not_found = True
while not_found:
    oned = sorted(list(set(str(k))))
    doub = sorted(list(set(str(k*2))))
    trip = sorted(list(set(str(k*3))))
    quad = sorted(list(set(str(k*4))))
    quin = sorted(list(set(str(k*5))))
    sext = sorted(list(set(str(k*6))))
    if oned == doub and doub == trip and trip == quad and quad == quin and quin == sext:
        print(k)
        not_found = False
    k += 1