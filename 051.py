"""
By replacing the 1st digit of the 2-digit number *3,
 it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
 this 5-digit number is the first example having seven primes among the ten generated numbers,
  yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
   Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
 is part of an eight prime value family.
"""

# Determine prime numbers
# Replace the same numbers with 0-9
# Count if those numbers are prime

# Check if the numbers in nums are prime and return the count of prime numbers
def checkprime(nums):
    c = 0
    ps = []
    for n in nums:
        prime = 1
        if n > 2:
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    prime = 0
                    break
        elif n < 2:
            prime = 0

        if prime == 1:
            ps.append(n)
            c += 1
    return c, ps

# Obtain replacement numbers
def repnums(x):
    xs = str(x)
    ls = list(xs)
    uq = list(set(ls))
    res_reps = []
    max_count = 0
    for i in uq:
        reps = []
        for k in range(10):
            r = int(xs.replace(i,str(k)))
            if len(str(r)) == len(xs):
                reps.append(r)

        count, ps = checkprime(reps)
        if count > max_count:
            res_reps = sorted(ps)
            max_count = count
    return max_count, res_reps


k = 13
not_found = True
while not_found:
    cnt, ns = repnums(k)
    if cnt == 8:
        not_found = False
        print(cnt,ns)
    k += 2
