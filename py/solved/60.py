"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

def is_prime(n):
    if n%2 == 0:
        return False
    i = 3
    while i*i < n:
        if n%i == 0:
            return False
        i += 2
    return True

def sieve(N):
    s = [1,1,0]+[0,1]*N
    for i in range(3,int(N**.5)+1,2):
        itr = i*2
        while itr < N:
            s[itr] += 1
            itr += i
    return [i for i in range(N) if s[i] == 0]

def prime_cc(p1,p2):
    return is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1)))

def sset(*lists):
    tmp = []
    for li in lists:
        tmp += li
    return [i for i in set(tmp) if all(i in li for li in lists)]

N = 10000
primes = sieve(N)
print "sieve created"
L = len(primes)
pairs = {i:[] for i in primes}

for i in xrange(L):
    for j in xrange(i+1,L):
        if prime_cc(primes[i],primes[j]):
            pairs[primes[i]].append(primes[j])
            pairs[primes[j]].append(primes[i])

print "pairs found"

m = 100000000000000
for a in primes:
    for b in pairs[a]:
        for c in sset(pairs[a],pairs[b]):
            for d in sset(pairs[a],pairs[b],pairs[c]):
                for e in sset(pairs[a],pairs[b],pairs[c],pairs[d]):
                    print a,b,c,d,e
                    m = min(m,sum((a,b,c,d,e)))
print m


