"""
The primes 3, 7, 109, and 673, are quite remarkable.
 By taking any two primes and concatenating them in any order the result will always be prime.
  For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
   792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from itertools import combinations

def checkprime(n):
    prime = 1
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            prime = 0
            break
    if prime == 1:
        return 1
    else:
        return 0

primes = [3,5]
not_found = True

max_sum = 100000
n = 7
k = 2
while not_found:

    prime = checkprime(n)
    if prime == 1:
        primes.append(n)
        buffer = []
        for p in primes[0:k]:
            p1 = int(str(n)+str(p))
            p2 = int(str(p)+str(n))

            ch1 = checkprime(p1)
            ch2 = checkprime(p2)

            if ch1 == 1 and ch2 == 1:
                buffer.append(p)

        k += 1

    buffer = sorted(buffer,reverse=True)
    nbuff = [[n]+buffer]
    if len(buffer) >= 5:
        for b in buffer:
            rbuff = [n,b]
            for c in buffer:
                if b != c:
                    p1 = int(str(b) + str(c))
                    p2 = int(str(c) + str(b))

                    ch1 = checkprime(p1)
                    ch2 = checkprime(p2)

                    if ch1 == 1 and ch2 == 1:
                        rbuff.append(c)

            nbuff.append(sorted(rbuff))

        checklists = [[n]+list(comb) for comb in combinations(buffer,4)]
        for checks in checklists:
            res = 0
            for lsts in nbuff:
                n_res = 0
                for xs in checks:
                    if xs in lsts:
                        n_res += 1
                if n_res == 5:
                    res += 1
            if res == 5:
                print(checks)
                print(sum(checks))
                not_found = False


    n += 2