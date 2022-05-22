"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_sq = 0; sum = 0
for i in range(1,101):      # Range of first 100 natural numbers
    sum_sq = sum_sq + i**2  # Generate sum of squares
    sum = sum + i           # Generate sum to be squared at the end

print(sum**2-sum_sq)