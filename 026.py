"""
A unit fraction contains 1 in the numerator.
 The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
 It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
 in its decimal fraction part.
"""
def dpoints(x):
    y = 1; i = 0; rec_list = [0]; re = 0
    # Number of recurrings is equal to remainder*10 of outcome starting with 1
    while y % x != 0:
        y = (y % x)*10
        i += 1
        rec_list.append(int(y/10))
        # If the list is growing, check when a string of 5 occurs again in the list for first time
        # Crude method, but for 1000, the approach is enough
        if (len(rec_list) > 16) and (rec_list[10:15] == rec_list[i-5:i]):
            re = 1
            break

    return rec_list, re

d = 0; max_n = 0; max_d = 0
while d < 1000:
    d += 1
    list, re = dpoints(d)
    if re == 1:
        if len(list) > max_n:
            max_n = len(list)
            max_d = d

print(max_d)