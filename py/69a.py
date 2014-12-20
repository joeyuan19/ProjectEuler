#!/bin/sh

# P69.py
# ProjectEuler
#
# Created by joe yuan on 9/30/11.
# Copyright 2011 Classified. All rights reserved.

import math


def phi(n):
    f = [0]*n
    for i in range(2,n):
        if f[i-1] == 0:
            if n%i == 0:
                f[i-1] += 1
                inc = 2
                c = i*inc
                while c < n:
                    f[c-1] += 1
                    inc += 1
                    c = i*inc
    f[-1] += 1
    return f.count(0)
max = 0
for i in range(3,10**6,2):
    print i
    n = i/phi(i)
    if n > max:
        max = n
        
print n