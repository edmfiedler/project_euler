"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
 For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
  which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
 n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
 the smallest number that can be written as the sum of two abundant numbers is 24.
  By mathematical analysis, it can be shown that all integers greater than 28123 can be written
   as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it is
     known that the greatest number that cannot be expressed as the sum of two abundant numbers
      is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def checkabundant(n):
    sum_div = 0
    for x in range(1,int(n/2)+1):
        if (n%x == 0):
            sum_div += x

    if sum_div > n:
        return 1
    else:
        return 0

ab = i = 0; abu_num = []
while i < 28124:
    i += 1
    c_ab = checkabundant(i)
    if c_ab == 1:
        ab = i
        abu_num.append(ab)

sums = []
for x in abu_num:
    for y in abu_num:
        sums.append(x+y)

sums = sorted(set(sums))
sums = sums[0:sums.index(28124)]
non_sum = 0; j = 0
for x in range(28124):
    if x == sums[j]:
        j+=1
    else:
        non_sum += x

print(non_sum)