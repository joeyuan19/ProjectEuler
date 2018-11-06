#!/bin/sh

# P26.py
# ProjectEuler
#
# Created by joe yuan on 5/17/11.
# Copyright 2011 Classified. All rights reserved.

def div(a,b):
    return a/b, a%b

def repeat(s):
    for i in range(1,len(s)):
        c = s[:i]
        most = 0
        for j in range(len(s)//i):
            if c != s[j:j+i]:
                len(c)
                break
def solve():
    a = 1
    m = 0
    for b in range(1,1000):
        a = 1
        a,R = div(a,b)
        x = [R]
        while R != 0:
            if R < b:
                R = R*10
                x.append(0)
            a,R = div(R,b)
            if R in x:
                d = len(x)-x.index(R)
                if d > m:
                    m = d
                    mi = b
                break
            else:
                x.append(R)
    return mi
 
from timer import time_function
print(time_function(solve))

