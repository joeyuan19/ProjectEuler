#!/bin/sh

# P53.py
# ProjectEuler
#
# Created by joe yuan on 3/29/11.
# Copyright 2011 Classified. All rights reserved.
from math import factorial

def solve():
    t = 0
    for n in range(0,101):
        for r in range(n+1):
            e = factorial(n)/(factorial(r)*factorial(n-r))
            if e > 1000000:
                t = t + 1
    return t

from timer import time_function
print(time_function(solve))
