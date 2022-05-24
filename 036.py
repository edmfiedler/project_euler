"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def checkpalindrome(n):
    if n == n[::-1]:
        return 1

sum_n = 0
for x in range(0,int(1e6)):
    b10 = checkpalindrome(str(x))
    b2 = checkpalindrome(str(bin(x))[2::])
    if b10 and b2 == 1:
        sum_n += x

print(sum_n)