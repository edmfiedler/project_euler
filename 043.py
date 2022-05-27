"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9
 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools

# Divisors required
divs = [2, 3, 5, 7, 11, 13, 17]

# Generate 0-9 pandigitals, note, 0123456789 is not pandigital in this case.
# Smallest pandigital, therefore, is 1023456789
p = "0123456789"
a = itertools.permutations(p)
j = [''.join(i) for i in a]
pans = []
for n in j:
    if len(str(int(n))) == 10:
        pans.append(n)

# Generate the digits to be divided
sum_pans = 0
for n in pans:
    prop = 1
    for d in range(1,8):
        dividend = int(n[d:d+3])
        divisor = divs[d-1]
        if dividend % divisor != 0:
            prop = 0
            break
    if prop == 1:
        sum_pans += int(n)

print(sum_pans)