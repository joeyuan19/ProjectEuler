#!/bin/sh

# P27.py
# ProjectEuler
#
# Created by joe yuan on 5/11/11.
# Copyright 2011 Classified. All rights reserved.
from math import sqrt


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

def f(n,a,b):
    return n**2 + a*n + b

def solve():
    most = 0
    A = 0
    B = 0
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            n = 0
            num = f(n,a,b)
            while prime(num):
                n += 1
                num = f(n,a,b)
            if n > most:
                most = n
                A = a
                B = b
    return A*B

from timer import time_function
print(time_function(solve))
