"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

# For speed, could make dictionary of factorials
def fac_digits(n):
    n = str(n); sum_fac = 0
    for j in n:
        fac = 1
        for k in range(2,int(j)+1):
            fac = fac * k

        sum_fac += fac

    return sum_fac

# Generate range, upper limit comes from 9999999 sum of factorial digits < number (highest possible)
sum_num = 0
for x in range(10,2540160):
    s_f = fac_digits(x)
    if x == s_f:
        sum_num += x

print(sum_num)