
"""
Product-sum numbers
Problem 88

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 * a2 * ... * ak.

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?
"""
from prime import sieve
from timer import time_function
from math import sqrt,log
from itertools import permutations

def prod(li):
    p = 1
    for i in li:
        p = p*i
    return p

def prime_factor(N,primes):
    f = [] 
    for p in primes:
        if p > N/2:
            return f
        i = 1
        while N%(p**i) == 0:
            i += 1
        if i > 1:
            f.append((p,i-1))
    return f

def gen_factors(N):
    for n in range(2,int(sqrt(N))+1):
        if N%n == 0:
            yield (n,N//n)
            if n <= N//n:
                for f in gen_factors(N//n):
                    yield (n,)+f

def solve():
    N = 12000
    N = int(N)
    UPPER = N+200  # originally 2*N
    primes = sieve(int(UPPER))
    mins = {k:(1e100,()) for k in range(2,N+1)}

    for n in range(4,UPPER+1):
        if n not in primes:
            for f in gen_factors(n):
                _k = len(f)
                s = sum(f)
                k = n - s + _k
                if k > N:
                    continue
                if n <= mins[k][0]:
                    mins[k] = (n,f) 
    return sum(set(i[0] for i in mins.values()))
from timer import time_function
print(time_function(solve))
#print(max(i[0] for i in mins.values()))
#print(sum(set(i[0] for i in mins.values())),time.time()-t)

#powers = [0]*len(primes)
#limits = [int(log(UPPER)/log(p)) for p in primes]

def inc(li,k,default=0):
    m = min(li)
    for i,j in enumerate(li):
        if j != m:
            li[i-1] += 1
            li = [default]*(i-1)+li[i-1:]
            return li
    return [default]*(len(li)-1) + [li[-1]+1]

def prod(li):
    p = 1
    for i in li:
        p = p*i
    return p

def bruteforce(N):
    m = []
    for k in range(2,N+1):
        s = [1]*k
        while prod(s) != sum(s):
            s = inc(s,k)
        m.append(sum(s))
    return sum(set(m)) 

# prod(a_i) - sum(a_i) = N, i = 1,...,k'
# k = k' + N
# P = prod(a_i)
# S = sum(a_i)
# P - S = k - k'
# P = S + k - k'
# at k', min is 2^k' = 2*k' + N 



def limitor(N):
    m = []
    for k in range(2,N+1):
        for _k in range(2,_k):
            s = [2]*_k
            while prod(s) < sum(s) + k-_k:
                if prod(s):
                    pass

graph = False
if graph:
    f = lambda x: x 
    from timer import time_function
    x,y = [],[]
    for N in range(2,24):
        #print(N)
        x.append(N)
        y.append(time_function(f,N)[-1])
        
    import matplotlib.pyplot as plt
    plt.plot(x,y)
    plt.xlabel('N')
    plt.ylabel('t')
    plt.show()

