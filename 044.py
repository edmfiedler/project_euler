"""
Pentagonal numbers are generated by the formula, Pn=n(3nā1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 ā 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk,
 for which their sum and difference are pentagonal and
  D = |Pk ā Pj| is minimised; what is the value of D?
"""
import math
# How can I check if a number is pentagonal? From wikipedia (sqrt(24*x+1)+1)/6 must be natural
def ispent(x):
    n = (math.sqrt(24*x+1)+1)
    if n % 6 == 0:
        return True
    else:
        return False

j = 2
not_found = True
# First instance will be smallest, loop until found
while not_found:
    p1 = j*(j*3-1)/2
    # More likely to find going in reverse
    for i in range(j-1,0,-1):
        p2 = i*(i*3-1)/2
        if ispent(p1+p2) == True and ispent(p1-p2) == True:
            result = p1-p2
            not_found = False
            break
    j += 1
print(int(result))