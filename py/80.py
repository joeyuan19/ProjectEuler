from decimal import *
getcontext().prec = 100

def converge(e,N):
    n = 1
    d = e[N-1]
    for i in xrange(N-2,-1,-1):
        n = n + d*e[i]
        d,n = n,d
    return d,n

def cont(s):
    a0 = a = int(s**.5)
    m = 0
    d = 1
    while int(a) != 2*a0:
        yield a
        m = d*a-m
        d = (s-m*m)/d
        a = int((a0+m)/d)
    yield a






