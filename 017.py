"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Set up dictionaries
dict_ones = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
}

dict_teens = {
    0:"ten",
    1:"eleven",
    2:"twelve",
    3:"thirteen",
    4:"fourteen",
    5:"fifteen",
    6:"sixteen",
    7:"seventeen",
    8:"eighteen",
    9:"nineteen"
}

dict_tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

sum_l = 0
for n in range(1,1001):
    num = str(f'{n:04}')
    if num[0] != '0':
        num_w = dict_ones[int(num[0])] + 'thousand'

    if num[3] != '0':
        num_w = dict_ones[int(num[3])]

    if num[2] == '1':
        num_w = dict_teens[int(num[3])]

    elif num[2] != '0':
        num_w = dict_tens[int(num[2])] + num_w

    if num[1] != '0':
        if num[2] == '0' and num[3] == '0':
            num_w = dict_ones[int(num[1])] + 'hundred'
        else:
            num_w = dict_ones[int(num[1])] + 'hundredand' + num_w

    sum_l += len(num_w)
    num_w = ''

print(sum_l)