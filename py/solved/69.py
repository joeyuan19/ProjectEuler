import time
debug = False

def sieve(n):
    s = [False,False,True]+[True,False]*(n/2-1)
    i = 3
    while i*i < n:
        if s[i]:
            for itr in xrange(2*i,n,i):
                s[itr] = False
        i += 2 
    return [i for i in xrange(n) if s[i]] 

def gcf(a,b):
    for n in xrange(min(a,b),0,-1):
        if a%n == 0 and b%n == 0:
            return n

def rels(n):
    s = 0
    for i in xrange(1,n):
        if gcf(i,n) == 1:
            s += 1
    return s

def fact(n,s=None):
    if s is None:
        s = sieve(int(n**.5)+1)
    _n = n
    while _n > 1:
        for p in s:
            if _n%p == 0:
                yield p
                while _n%p == 0:
                    _n = _n/p
                break


N = 10**6
L = N+1
s = sieve(L)
space = [0]*L
space[1] = 1
idx = [i for i in xrange(L)]
for p in s:
    space[p] = p-1
    if 2*p < L:
        space[2*p] = (2-p%2)*(p-1)
    e = 1
    while p**e < L:
        space[p**e] = p**e-p**(e-1)
        e += 1


for i in xrange(2,L):
    if space[i] == 0:
        print i 
        p = i
        for p in s:
            if i%p == 0:
                d = gcf(p,i/p)
                space[i] = int(space[p]*space[i/p]*(float(d)/space[d]))
                break
    elif 2*i < L:
        space[2*i] = (2-i%2)*space[i]

print max((float(i)/space[i],i) for i in xrange(2,L))
print "Time:",time.time()-start,"s"
if debug:
    print "Creating brute force solution"
    solution = [rels(i) for i in xrange(2,L)]
    space = space[2:]
    print solution
    no_error = True
    for i in xrange(L-2):
        if solution[i] != space[i]:
            no_error = False
            print "Error on",i+2,"Should be",solution[i],"but is",space[i]
        

    if no_error:
        print "Looks good!"


"""
Notable solution found afterward in the forums
N = 10**6
s = 1
for p in sieve(N):
    if s*p > N:
        print s
        break
    s = s*p

import sys
sys.exit()
"""
