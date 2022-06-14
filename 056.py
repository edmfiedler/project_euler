"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
 one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

max_sum = 0
for a in range(100):
    for b in range(100):
        num = a**b
        num_str = str(num)
        val = 0
        for d in num_str:
            val += int(d)

        if val > max_sum:
            max_sum = val

print(max_sum)