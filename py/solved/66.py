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

N = 1000
m = -1
_D = -1
for D in xrange(2,N+1):
    if int(D**.5) == D**.5:
        continue
    seq = [i for i in cont(D)]
    seq = [seq[0]]+seq[1:]*100
    for i in xrange(1,100):
        n,d = converge(seq,i)
        if n*n - D*d*d == 1:
            break
    if n > m:
        _D = D
        m = n
print _D



