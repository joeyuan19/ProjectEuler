#!/bin/sh

# P30.py
# ProjectEuler
#
# Created by joe yuan on 3/27/11.
# Copyright 2011 Classified. All rights reserved.


def powersum(n,p=5):
    return sum(int(i)**p for i in str(n))

def main(N):
    return sum(i for i in range(11,N) if i == powersum(i))

from timer import time_function

def solve(P):
    n = 10
    s = 0
    m = 9**P
    for e in range(1,10):
        if e*m < 10**(e-1):
            N = e
            break
    lim = 10**(N-1)
    while n < lim: 
        p = powersum(n,P)
        if p == n:
            s += n
        if p > n:
            n = (n//10 + 1)*10
        else:
            n += 1
    return s
print(time_function(solve,5))
