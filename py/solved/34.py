#!/bin/sh

# P34.py
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.

from math import factorial as f

def f_sum(n):
    return sum(f(int(i)) for i in str(n)) 

def solve():
    m = f(9)
    for i in range(1,10):
        if i*m < 10**(i-1):
            lim = 10**(i-1)
            break
    n = 10
    s = 0
    while n < lim: 
        p = f_sum(n)
        if p == n:
            s += n
        if p > n:
            n = (n//10 + 1)*10
        else:
            n += 1
    return s

from timer import time_function
print(time_function(solve))
