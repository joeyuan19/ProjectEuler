from totient import totients

def gcf(a,b):
    for n in xrange(min(a,b),0,-1):
        if a%n == 0 and b%n == 0:
            return n

def rels(n):
    s = 0
    for i in xrange(1,n):
        if gcf(i,n) == 1:
            yield i

def coprimes(d,n,L):
    q = [(d,n)]
    quit = 0
    while len(q) > 0:
        quit += 1
        nxt = q.pop()
        if nxt[1] >= L or nxt[0] > L or nxt[1] > nxt[0]:
            continue
        else:
            yield nxt
            q.append((2*nxt[0]-nxt[1],nxt[0]))
            q.append((2*nxt[0]+nxt[1],nxt[0]))
            q.append((nxt[0]+2*nxt[1],nxt[1]))


c = 0
L = 12000
t = sum(i for i in totients(L))
d = 2
n = 1
a = 0
for i,j in coprimes(d,n,L):
    print str(100.*a/t)[:5]+"% of space searched\r",
    if .5 > float(j)/i > 1./3:
        c += 1
    a += 1
d = 3
n = 1
for i,j in coprimes(d,n,L):
    print str(100.*a/t)[:5]+"% of space searched\r",
    if .5 > float(j)/i > 1./3:
        c += 1
    a += 1
print c
