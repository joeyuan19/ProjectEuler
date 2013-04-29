#!/bin/sh

# P21.py
# ProjectEuler
#
# Created by joe yuan on 3/10/11.
# Copyright 2011 Classified. All rights reserved.
def d(n):
    t = 0
    for c in range(1,n/2 + 1):
        if n%c == 0:
            t = t + c
    return t

q = []
for a in range(1,10001):
    b = d(a)
    if d(a) == b and d(b) == a and a != b:
        q.append(a)
        q.append(b)
sum = 0
for w in q:
    sum = sum + w
print sum/2
        

