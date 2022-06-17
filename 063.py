"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

count = 0
power = 1
while len(str(9**power)) == power:
    n = 1
    while n < 10:
        if len(str(n**power)) == power:
            count += 1
        n += 1
    power += 1
print(count)
