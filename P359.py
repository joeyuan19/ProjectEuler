#!/bin/sh

# 359.py
# ProjectEuler
#
# Created by joe yuan on 11/21/11.
# Copyright 2011 Classified. All rights reserved.


from math import sqrt

N = 71328803586048.
n = 1

r = 0
f = 0
p = [[]]



while (n < N):
    print n
    if len(p[f]) == 0:
        p[f].append(n)
        print f, " ", len(p[f])
        n += 1
        f = 0
    elif len(p[f]) == 0:
        c = sqrt(P[f][len(p[f]) - 1] + n)
        if c == int(c):
            P[f].append(n)
            print f, " ", len(p[f])
            n += 1
            f  = 0
    else:
        f += 1
        if f >= len(p):
            p.append([])
    
while (f < N + 1):
    if N%f == 0:
        r = N/f
        sum += P[f][r]
    f += 1
    