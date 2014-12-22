from prime import sieve

"""
OEIS series A00872

Given by a(n)

"""

def pfact(n,s):
    c = 0
    for p in s:
        if p > n:
            break
        elif n%p == 0:
            c += p
    return c

def count(n,factor_sums,counts):
    return int((1./n)*sum(factor_sums[k-1]*counts[n-k-1] for k in xrange(1,n+1)))

N = 10
L = N+1
s = sieve(L)
f = [pfact(i,s) for i in xrange(L)]
print f
c = [1,0]
for n in xrange(2,L): 
    a = count(n,f,c)
    c.append(a)
    print n,a
    if a > 5000:
        print "Answer:",n
        break

