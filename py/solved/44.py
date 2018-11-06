# !/bin/sh

# P44.py
# ProjectEuler
#
# Created by joe yuan on 5/17/11.
# Copyright 2011 Classified. All rights reserved.
from numpy import abs
import sys

def p(n):
    return n*(3*n - 1)/2

def ptest(n,j=0):
    index = j + 1
    while 1:
        if n == p(index):
            return True
        elif n < p(index):
            return False
        else:
            index += 1
def solve():
    k = 1
    while 1:
        for j in range(1,k):
            if ptest(abs(p(k) - p(j))):
                if ptest(p(k) + p(j)):
#                    print j,k,abs(p(k) - p(j))
                    sys.exit(0)
        k += 1

from timer import time_function
print(time_function(solve))

"""
min = 70
k = 1
while 1:
    j = k + 1
    c = p(j)
    n = p(k)
    while 1:
        if abs(c - n) > min:
            break
        if ptest(abs(c - n)):
            if ptest(c+n):
                if abs(c - n) < min:
                    min = abs(c - n)
        j += 1
        n = p(j)
    print k,min
    k += 1
"""    















"""
from numpy import abs

def p(n):
    return n*(3*n - 1)/2

def ptest(n,j=0):
    index = j + 1
    while 1:
        if n == p(index):
            return True
        elif n < p(index):
            return False
        else:
            index += 1

start = 1
end = 100
inc = 100
pent = [p(i) for i in range(start,end+1)]
index = 0

while 1:
    for j,i in enumerate(pent[index:]):
        for l,k in enumerate(pent):
            print i,k
            s = i + k
            d = abs(i-k)
            x = max([index+j,l])
            if ptest(s,x):
                if ptest(d):
                    print i, k, "diff =", d, "sum =", s
                    u = True
                    break
            u = False
        if u:
            break
    if u:
        break
    start += inc
    end += inc
    pent += [p(i) for i in range(start,end+1)]
    index += j

"""
