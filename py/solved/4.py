#!/bin/sh

# P4.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

def pall(n):
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            return False
    return True

def solve():
    pal = []
    t = 0
    for i in range(100,1000):
        for c in range((100 + t),1000):
            n = list(str(i*c))
            if pall(n):
                pal.append(i*c)
        t = t + 1

    pal.sort()
    return pal[-1]

from timer import time_function
print(time_function(solve))
