"""
Consider quadratic Diophantine equations of the form:

x**2 – D*y**2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3**2 – 2×2**2 = 1
2**2 – 3×1**2 = 1
9**2 – 5×4**2 = 1
5**2 – 6×2**2 = 1
8**2 – 7×3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

# Fastest way to obtain the fundamental solution to Pell's equation is by finding the trying the continued fractions of the d**0.5

max_x = 0
for n in range(2,1000+1):
    sq = n**0.5
    if int(sq)/sq == 1:
        continue
    a = int(sq)
    m = 0
    d = 1
    
    seq = [a]
    not_found = True
    # A period ends when the value is doubled from original
    while not_found:
        # Obtain the value that +- sqrt in fraction
        m = d*a-m
        # Obtain the new denominator
        d = (n-m**2)/d
        # Obtain the continued fraction value
        a = int((int(sq)+m)/d)
        seq.append(a)
        
        # Obtain numerator and denominator of generated sequence continued fraction
        den = a
        i = 1
        for x in seq[1:-1][::-1]:
            num = den*x+i
            i = den
            den = num
        num = den*seq[0]+i
        
        # Check if diophantine equation is fulfilled
        if num**2-n*den**2 == 1:
            if num > max_x:
                max_x = num
                max_d = n
            not_found = False

print(max_d)
