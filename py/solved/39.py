#!/bin/sh

# P39.py
# ProjectEuler
#
# Created by joe yuan on 5/22/11.
# Copyright 2011 Classified. All rights reserved.

from time import clock

def pyth(a,b,c):
    return a**2 + b**2 == c**2

def perim(p,a,b=0,c=0):
    if a+b+c != p:
        return False
    else:
        return True
def solve():
    most = []
    for p in range(1001):
        print(p)
        dummy = [p]
        for a in range(1,p):
            for b in range(a,p):
                c = p - (a+b)
                if not perim(p,a,b,c):
                    break
                if pyth(a,b,c):
                    dummy.append((a,b,c))
        if len(dummy) > len(most):
            most = dummy
    return most

from timer import time_function
print(time_function(solve))
