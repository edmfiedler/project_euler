"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though
 the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular
  number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
 but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

# Technically could just replace all non-minimal sequences with 2 letters
# However, more fun to create a roman numeral converter

with open('txt_files/p089_roman.txt') as f:
    lines = f.readlines()

rom_nums = []
for l in lines:
    if '\n' in l:
        rom_nums.append(l[:-1])
    else:
        rom_nums.append(l)

"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""

# Obtain conversion from roman numeral to number
nums = []
for r in rom_nums:
    rev = r[::-1]
    num = 0
    pv = 0
    for l in rev:
        if l == 'I':
            v = 1
        if l == 'V':
            v = 5
        if l == 'X':
            v = 10
        if l == 'L':
            v = 50
        if l == 'C':
            v = 100
        if l == 'D':
            v = 500
        if l == 'M':
            v = 1000

        if v < pv:
            num -= v
        else:
            pv = v
            num += v
    nums.append(str(num))

# Obtain conversion from number to correct roman numeral
corr_rom = []
for n in nums:
    rev = n[::-1]
    rom = ''
    for c, r in enumerate(rev):
        if c == 0:
            if int(r) < 4:
                rom = 'I'*int(r) + rom
            if int(r) == 4:
                rom = 'IV' + rom
            if int(r) > 4 and int(r) < 9:
                rom = 'V' + 'I'*(int(r)-5) + rom
            if int(r) == 9:
                rom = 'IX' + rom
        if c == 1:
            if int(r) < 4:
                rom = 'X' * int(r) + rom
            if int(r) == 4:
                rom = 'XL' + rom
            if int(r) > 4 and int(r) < 9:
                rom = 'L' + 'X' * (int(r) - 5) + rom
            if int(r) == 9:
                rom = 'XC' + rom
        if c == 2:
            if int(r) < 4:
                rom = 'C' * int(r) + rom
            if int(r) == 4:
                rom = 'CD' + rom
            if int(r) > 4 and int(r) < 9:
                rom = 'D' + 'C' * (int(r) - 5) + rom
            if int(r) == 9:
                rom = 'CM' + rom
        if c == 3:
            rom = 'M' * int(r) + rom
    corr_rom.append(rom)

saved = 0
for c, r in enumerate(rom_nums):
    diff = len(r)-len(corr_rom[c])
    saved += diff

print(saved)
