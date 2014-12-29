def gcd(a,b):
    if a == 0 or a == b:
        return b
    elif b == 0:
        return a
    elif a%2 == 0 and b%2 == 0:
        return 2*gcd(a/2,b/2)
    elif a%2 == 1 and b%2 == 1:
        return gcd(abs(a-b)/2,min(a,b))
    elif a%2 == 1:
        return gcd(b/2,a)
    elif b%2 == 1:
        return gcd(a/2,b)

def pythagorean_triple(m,n):
    return m*m - n*n, 2*m*n, n*n + m*m

def dot(k,li):
    return [k*i for i in li]

N = 1500000
L = N+1
space = [0]*(L)
for m in xrange(1,int(L**.5)):
    for n in xrange(1,m):
        if (m-n)%2 == 1 and gcd(n,m) == 1:
            k = 1
            tri = pythagorean_triple(m,n)
            while sum(k*i for i in tri) <= L:
                space[sum(k*i for i in tri)] += 1
                k += 1

print space.count(1)


