"""
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both
diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral
for which the ratio of primes along both diagonals first falls below 10%?
"""

d = 3
prev = 1
not_Found = True
tot_primes = 0
tot_diag = 1

# Run until found
while not_Found:
  tot_diag += 4
  # The total number of items in the outer ring
  leng = 2*d+2*(d-2)
  buf = [x+prev for x in range(1,leng+1)]
  # Numbers located in corners
  corners = buf[d-2::d-1]
  # Check if corner items are prime
  for n in corners:
    prime = 1
    for m in range(2,int(n**0.5)+1):
      if n % m == 0:
        prime = 0
        break
    if prime == 1:
      tot_primes += 1
  # Check if condition is fulfilled
  if tot_primes/tot_diag < 0.1:
    not_Found = False
  prev = buf[-1]
  d += 2

print(d-2)
