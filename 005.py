"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def checkDivisibility(i):
    for j in range(1,21):   # Range of numbers to check divisibility for
        if (i%j == 0):
            if (j==20):     # If it arrives at the highest, then it is the smallest number
                print(i)
                return 0
        else:
            return 1

i = 20
while True:
    i = i + 1
    if checkDivisibility(i) == 0:   # Condition for when the divisible number has been found
        break