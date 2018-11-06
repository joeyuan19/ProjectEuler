#!/bin/sh

# P56.py
# ProjectEuler
#
# Created by joe yuan on 3/31/11.
# Copyright 2011 Classified. All rights reserved.


def digit_sum(n):
    n1 = str(n)
    sum = 0
    for i in n1:
        sum = sum + int(i)
    return sum

def solve():
    i = 0
    for a in range(101):
        for b in range(101):
            #print a,'^',b
            c = digit_sum(a**b)
            if c > i:
                i = c
                
    return i

from timer import time_function
print(time_function(solve))
