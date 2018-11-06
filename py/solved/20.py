#!/bin/sh

# P20.py
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.

def factorial(N):
    if N < 2:
        return 1
    else:
        return N*factorial(N-1)

def solve():
    return sum(int(i) for i in str(factorial(100)))

from timer import time_function
print(time_function(solve))
