import sys
import time
from prime import sieve

N = 10
L = N+1

sieves = {i:[0] for i in xrange(1,L)}

for i in xrange(1,L):
    sieves[i] = [j/i for j in xrange(1,i+1)]*(L/i)+[0]*(L%i)

for s in sieves:
    print s,sieves[s],len(sieves[s])
print "done"


"""
start = time.time()
def sset(*lis):
    a = set(lis[0])
    for li in lis[1:]:
        a = a.intersection(set(li))
    return a

N = 10**int(sys.argv[1])#**6
s = sieve(N)
print "sieve done. Took",time.time()-start,"s"
data = {}

tmp = time.time()
for i in xrange(2,N+1):
    data[i] = [1,i]
    for j in s:
        if j*2 > i:
            break
        elif i%j == 0:
            data[i].append(j)
print "factors done. Took ",time.time()-tmp,"s"
rel = {}
tmp = time.time()
for a in data:
    rel[a] = [1]
    for b in data:
        if a <= b: break
        if a > b and len(sset(data[a],data[b])) == 1:
            rel[a].append(b)
rel[1] = [1]
print "rels done.  Took ",time.time()-tmp,"s"

tmp = time.time()
print max((float(i)/len(rel[i]),i) for i in rel)
print "Found max. Took",time.time()-tmp,"s"
print "Time:",time.time()-start,"s"
"""
