import time
debug = False

def sieve(n):
    s = [False,False,True]+[True,False]*(n//2-1)
    i = 3
    while i*i < n:
        if s[i]:
            for itr in range(2*i,n,i):
                s[itr] = False
        i += 2 
    return [i for i in range(n) if s[i]] 

def gcf(a,b):
    for n in range(min(a,b),0,-1):
        if a%n == 0 and b%n == 0:
            return n

def rels(n):
    s = 0
    for i in range(1,n):
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
idx = [i for i in range(L)]
for p in s:
    space[p] = p-1
    if 2*p < L:
        space[2*p] = (2-p%2)*(p-1)
    e = 1
    while p**e < L:
        space[p**e] = p**e-p**(e-1)
        e += 1


for i in range(2,L):
    if space[i] == 0:
        #print i 
        p = i
        for p in s:
            if i%p == 0:
                d = gcf(p,i/p)
                space[i] = int(space[p]*space[i//p]*(float(d)/space[d]))
                break
    elif 2*i < L:
        space[2*i] = (2-i%2)*space[i]

#print max((float(i)/space[i],i) for i in range(2,L))
#print "Time:",time.time()-start,"s"
if debug:
    #print "Creating brute force solution"
    solution = [rels(i) for i in range(2,L)]
    space = space[2:]
    #print solution
    no_error = True
    for i in range(L-2):
        if solution[i] != space[i]:
            no_error = False
            print("Error on",i+2,"Should be",solution[i],"but is",space[i])
    if no_error:
        print("Looks good!")


"""
Notable solution found afterward in the forums
N = 10**6
s = 1
for p in sieve(N):
    if s*p > N:
        #print s
        break
    s = s*p

import sys
sys.exit()
"""



"""
old 69.py file
import sys
import time
from prime import sieve

N = 10
L = N+1

sieves = {i:[0] for i in range(1,L)}

for i in range(1,L):
    sieves[i] = [j/i for j in range(1,i+1)]*(L/i)+[0]*(L%i)

for s in sieves:
    #print s,sieves[s],len(sieves[s])
#print "done"


"""
start = time.time()
def sset(*lis):
    a = set(lis[0])
    for li in lis[1:]:
        a = a.intersection(set(li))
    return a

N = 10**int(sys.argv[1])#**6
s = sieve(N)
#print "sieve done. Took",time.time()-start,"s"
data = {}

tmp = time.time()
for i in xrange(2,N+1):
    data[i] = [1,i]
    for j in s:
        if j*2 > i:
            break
        elif i%j == 0:
            data[i].append(j)
#print "factors done. Took ",time.time()-tmp,"s"
rel = {}
tmp = time.time()
for a in data:
    rel[a] = [1]
    for b in data:
        if a <= b: break
        if a > b and len(sset(data[a],data[b])) == 1:
            rel[a].append(b)
rel[1] = [1]
print("rels done.  Took ",time.time()-tmp,"s")
