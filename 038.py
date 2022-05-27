"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
 We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
 which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
 of an integer with (1,2, ... , n) where n > 1?
"""

# Form the condition
# Maximum will be where len(i*1) + len(i*2) = 9
# 1 to 9999

mpand = 0
for i in range(1,9999):
    n = 1
    pand = ""
    while len(pand) < 9:
        pr = n * i
        pand += str(pr)
        n += 1
    # No zeros in product
    if "0" in pand:
        continue
    if len(list(set(pand))) == 9 and len(pand) == 9:
        if int(pand) > mpand:
            mpand = int(pand)

print(mpand)