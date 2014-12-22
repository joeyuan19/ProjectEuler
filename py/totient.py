from prime import sieve

def totient(n):
    s = sieve(n)
    t = float(n)
    for p in s:
        if n%p == 0:
            t *= (1-1./p)
    return int(t)

def gcf(a,b):
    for n in xrange(min(a,b),0,-1):
        if a%n == 0 and b%n == 0:
            return n

def totients(N):
    L = N+1
    t = [i for i in xrange(L)]
    s = sieve(L)
    for p in s:
        for itr in xrange(p,L,p):
            t[itr] = t[itr]*(1-1./p)
    return [int(i) for i in t]

def totients2(N):
    L = N+1
    s = sieve(L)
    space = [0]*L
    space[1] = 1
    idx = [i for i in xrange(L)]
    for p in s:
        space[p] = p-1
        e = 2
        while p**e < L:
            space[p**e] = (p**(e-1))*space[p] 
            e += 1
        itr = 2*p
        while itr < L:
            space[itr] = (2-p%2)*space[itr/2]
            itr = itr*2
    i = 0
    while i < len(s):
        j = i+1
        while j < len(s) and s[i]*s[j] < L:
            space[s[i]*s[j]] = space[s[i]]*space[s[j]]
            j += 1
        i += 1

    for i in xrange(2,L):
        if space[i] == 0:
            for p in s:
                if i%p == 0:
                    d = gcf(p,i/p)
                    space[i] = int(space[p]*space[i/p]*(float(d)/space[d]))
                    if 2*i < L:
                        space[2*i] = (2-i%2)*space[i]
                    e = 2
                    while i**e < L:
                        if space[i**e] == 0:
                            space[i**e] = (i**(e-1))*space[i]
                            e += 1
                    break
        elif 2*i < L:
            space[2*i] = (2-i%2)*space[i]
    return space
