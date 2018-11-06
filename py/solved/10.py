#!/bin/sh

# P10.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

def sieve(N):
    s = [0,0,1]+[1,0]*(N//2)
    i = 3
    while i*i < N:
        if s[i]:
            for itr in range(i*2,N,i):
                s[itr] = 0
        i += 2
    return [i for i in range(N) if s[i]==1]

def prime(f):
    prime = [2]
    for i in range(3,f,2):###<----modify to range(3,f) for primes up to f
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u:
            print(i)
            prime.append(i)
    return prime

def solve():
    return sum(sieve(2000000))

from timer import time_function
print(time_function(solve))
