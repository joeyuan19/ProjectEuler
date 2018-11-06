#!/bin/sh

# P50.py
# ProjectEuler
#
# Created by joe yuan on 5/22/11.
# Copyright 2011 Classified. All rights reserved.

def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(N**0.5)+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]

def solve():
    p = Sieve(1000000)
    highest = p[-1]
    count = 0

    for j in range(len(p)):
        s = 0
        for k,i in enumerate(p[j:]):
            s += i
            if s in p:
                if k + 1  > count:
                    count = k + 1
                    index = s
            elif s > highest:
                break

    return index, count
from timer import time_function
print(time_function(solve))
