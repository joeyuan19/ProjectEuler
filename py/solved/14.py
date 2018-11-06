#!/bin/sh

# P14.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

def collatz(n):
    return 3*n+1 if n%2 else n//2

def solve(N):
    C = {1:1}
    for n in range(2,N):
        a = []
        while n not in C:
            a.append(n)
            n = collatz(n)
        _c = C[n]
        for i,n in enumerate(a[::-1]):
            C[n] = _c + i + 1
    mk,mv = -1,-1
    for k,v in C.items():
        if v > mv:
            mv = v
            mk = k
    return mk

def solve_bf():
    x = []
    for i in range(1000000,0,-1):
        d = []
        d.append(i)
        c = i
        while c != 1:
            if c%2 == 0:
                c = c/2
            else:
                c = 3*c + 1
            d.append(c)
        x.append([len(d),d[0]])
    x.sort()
    return x[-1]

from timer import time_function
print(time_function(solve,int(1e6)))


