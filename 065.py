"""
Sum of digits in the numerator of the 100th convergent of the continued fraction for e
"""

c_fracs = [2]
for x in range(1,50):
    c_fracs.append(1)
    c_fracs.append(2*x)
    c_fracs.append(1)
c_fracs = c_fracs[0:100]
print(c_fracs)

x0 = c_fracs[-1]
den = x0
i = 1
for n in c_fracs[1:-1][::-1]:
    num = den*n+i
    i = den
    den = num
    
num = den*2+i

num = str(num)
sum_n = 0
for x in num:
    sum_n += int(x)
print(sum_n)
