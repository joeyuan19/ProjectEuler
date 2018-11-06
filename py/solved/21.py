#!/bin/sh

# P21.py
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.


# accidently deleted...drunk...but i used a def d(n):
# to solve for the avlues for a and b then comparison and check for equality.
# 31626

# 4/12/17 - rewriting
from math import sqrt

def d(n):
    s = 1
    for i in range(2,int(sqrt(n)) + 1):
        if n%i == 0:
            s += i + n//i
    return s

def solve(N):
    data = {}
    for a in range(N):
        _d = d(a)
        data[a] = _d
    s = []
    for a in range(N):
        if data[a] < N:
            if data[a] != a and data[data[a]] == a:
                s.append(a)
        else:
            if data[a] == d(data[a]):
                s.append(a)
    return sum(set(s))

from timer import time_function
print(time_function(solve,10000))

