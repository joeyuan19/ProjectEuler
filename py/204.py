#!/bin/sh

# P204.py
# ProjectEuler
#
# Created by joe yuan on 5/23/11.
# Copyright 2011 Classified. All rights reserved.

def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(N**.5)+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]

def primefactor(f):
    return [i for i in Sieve(f) if f%i == 0]
i = 100
count = 0
while i < 10**9:
    print i
    if len(primefactor(i)) <= 100:
        count += 1
    i += 1