#!/bin/sh

# test.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

from math import *

def primefactor(f):
    if f%2 == 0:
        factors = [2]
    else:
        factors = []
    for i in range(3,f/2 + 1,2):
        if prime(i) and f%i == 0:
            factors.append(i)
    if len(factors) == 0:
        factors = [f]
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


for i in range(1,100):
    print i,primefactor(i)