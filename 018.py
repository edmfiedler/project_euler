"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""
import numpy as np

triangle ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

n_rows = 15; lat = np.zeros((n_rows,n_rows))

flat_triangle = []
for n in triangle:
    if str.isspace(n) == False:
        flat_triangle.append(n)

nums = []
for d in range(0,len(flat_triangle),2):
    num = 10*int(flat_triangle[d])+int(flat_triangle[d+1])
    nums.append(num)

i = 0; i_ = 0
for x in nums:
    lat[i,i_] = x
    i_ += 1
    if i_ > i:
        i += 1
        i_ = 0

for rows in reversed(range(n_rows-1)):
    for cols in range(rows+1):
        if lat[rows,cols]+lat[rows+1,cols] >= lat[rows,cols]+lat[rows+1,cols+1]:
            lat[rows,cols] = lat[rows,cols]+lat[rows+1,cols]
        else:
            lat[rows,cols] = lat[rows,cols] + lat[rows+1,cols+1]

print(int(lat[0,0]))
