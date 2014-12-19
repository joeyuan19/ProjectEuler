def cont(s):
    a0 = a = int(s**.5)
    m = 0
    d = 1
    p = 0
    while int(a) != 2*a0:
        m = d*a-m
        d = (s-m*m)/d
        a = int((a0+m)/d)
        p += 1
    return p

from decimal import *
getcontext().prec = 100

N = 10000
s = 0
for i in range(2,N+1):
    if int(i**.5) != i**.5 and cont(i)%2 == 1:
        s += 1

print s
