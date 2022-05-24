"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def factorial(n):
    prod = 1
    for x in range(1,n+1):
        prod = prod*x
    return prod

sum_digits = sum([int(x) for x in str(factorial(100))])
print(sum_digits)