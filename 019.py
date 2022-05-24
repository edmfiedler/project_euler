"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
        but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# YYYY-MM-DD

# Sunday is 7
y = 1900; m = 1; d = 1; cnt = 1; n_sun = 0
while y < 2001:
    cnt += 1
    d += 1
    if d > 7:
        d = 1

    if (m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12):
        if cnt > 31:
            cnt = 1
            m += 1
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11):
        if cnt > 30:
            cnt = 1
            m += 1
    else:
        if (y%4 =lines[it1+1:it2]= 0) and (y%100 != 0):
            if cnt > 29:
                cnt = 1
                m += 1
        elif (y%4 == 0) and (y%100 == 0) and (y%400==0):
            if cnt > 29:
                cnt = 1
                m += 1
        else:
            if cnt > 28:
                cnt = 1
                m += 1

    if (cnt == 1) and (d == 7) and (y >= 1901):
        n_sun += 1

    if (cnt == 31) and (m == 12):
        m = 1
        cnt = 0
        y = y + 1

print(n_sun)