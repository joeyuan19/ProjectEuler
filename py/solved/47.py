#!/bin/sh

# P47.py
# ProjectEuler
#
# Created by joe yuan on 3/29/11.
# Copyright 2011 Classified. All rights reserved.
from math import *

def primefactor(f):
    if f%2 == 0:
        factors = [2]
    elif prime(f):
        factors = [f]
    else:
        factors = []
    for i in range(3,f/2 + 1,2):
        if f%i == 0:
            if prime(i):
                factors.append(i)
    return factors   

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(sqrt(n)) + 1,2):
        if n%i == 0:
            return False
    return True

d = []
i = 1
while len(d) != 4:
    if len(primefactor(i)) == 4:
        d.append(i)
    else:
        d = []
    i = i + 1
    print d
print d