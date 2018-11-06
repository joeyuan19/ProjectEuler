#!/bin/sh

# P23.py
# ProjectEuler
#
# Created by joe yuan on 3/11/11.
# Copyright 2011 Classified. All rights reserved.


def factor_list(N):
    f = {i:[1] for i in range(2,N)}
    for i in range(2,N):
        for j in range(2*i,N,i):
            f[j].append(i)
    return f

def solve(N):
    ab = []
    for k,v in factor_list(N).items():
        if k < sum(v):
            ab.append(k)
    s = [0]*(2*ab[-1]+1)
    for i,a in enumerate(ab):
        for b in ab[i:]:
            s[a+b] = 1
    a = 0
    j = 0
    while j < N:
        if s[j] == 0:
            a += j
        j += 1
    return a


from timer import time_function
print(time_function(solve,28123))

"""
# Old brute force:
def factor(f):
    factor = []
    s = 0
    for i in range(1,f//2 + 1):###<----modify to range(3,f) for primes up to f
        if f%i == 0: 
            s = s + i
    if s > f:
        return True
    else:
        return False

def abundance_list(f):
    ab = []
    for i in range(f+1):
        if factor(i):
           ab.append(i)
    return ab

def ab_sum_test(f,ab):
    for c in ab:
        if (f - c) in ab:
            return True
    return False

def solve(N):
    ab = abundance_list(N)
    s = 0
    for i in range(N):
        if not ab_sum_test(i,ab):
            s = s + i
    return s

### Try 4179871 
### last output was: 20161 why would limit be 28000 if the last one is that????

"""
