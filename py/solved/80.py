from decimal import *
getcontext().prec = 121

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

N = 100
c = 0
A = 10000
for j in xrange(2,N+1):
    if int(j**.5) == j**.5:
        continue
    seq = [i for i in cont(j)]
    seq = [seq[0]]+seq[1:]*A
    last = ''
    i = 1000
    n,d = converge(seq,i)
    s = str( Decimal(n) / Decimal(d) )
    while i < A:
        n,d = converge(seq,i)
        last = s
        s = str( Decimal(n) / Decimal(d) )
        if last == s:
            break
        i += 1
        if i > 5:
            break
    p = sum(int(i) for i in s[:101] if i.isdigit())
    print j,p
    c += p 
print c



