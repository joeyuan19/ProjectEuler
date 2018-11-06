#!/bin/sh

# P37.py
# ProjectEuler
#
# Created by joe yuan on 3/27/11.
# Copyright 2011 Classified. All rights reserved.

from math import *

def sieve(N):
    s = [0,0,1]+[1,0]*(N//2)
    i = 3
    while i*i < N:
        if s[i]:
            for itr in range(i*2,N,i):
                s[itr] = 0
        i += 2
    return [i for i in range(N) if s[i]==1]


def prime(n,P,PN):
    if n > PN:
        P = sieve(10*n)
        PN = 10*n
    return n in P

def trunc(n,P,PN):
    s = str(n)
    l = len(s)
    return all(prime(int(s[i:]),P,PN) for i in range(l)) and all(prime(int(s[:l-i]),P,PN) for i in range(1,l))

def main():
    PN = 1000000
    P = sieve(PN)
    ti = 4
    tp = 0
    s = 0
    while tp != 11:
        try:
            t = P[ti]
        except:
            P = sieve(PN*10)
            PN = PN*10
            t = P[ti]
        print(t)
        if trunc(t,P,PN):
            print(t)
            s = s + t
            tp = tp + 1
        ti += 1
    return s
            
from timer import time_function
print(time_function(main))
            
