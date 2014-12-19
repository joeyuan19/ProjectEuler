#!/bin/sh

# nineteen.py
# ProjectEuler
#
# Created by joe yuan on 5/22/11.
# Copyright 2011 Classified. All rights reserved.

from numpy import sqrt

def digit_sum(n):
    s = str(n)
    sum = 0
    while len(s) > 2:
        for i in s:
            sum += int(i)
        s = str(sum)
        sum = 0
    return int(s)

def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(sqrt(N))+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]


p = Sieve(1000000)
p19 = []
for i in p:
    if digit_sum(i) == 19:
        p19.append(i)
        
for i in p19:
    print i
print len(p19)