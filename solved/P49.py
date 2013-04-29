#!/bin/sh

# P49.py
# ProjectEuler
#
# Created by joe yuan on 5/21/11.
# Copyright 2011 Classified. All rights reserved.



####WOULD BE SPED UP BY MAKING LISTS OF PERM TRIOS FIRST THEN CHECK ALGEBRAIC SUM


from numpy import sqrt
from itertools import permutations as perm


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
    p = []
    for j,i in enumerate(x):
        if i == 0:
            p.append(j+1)
    return p
    
def P(i):
    i = str(i)
    list = [int(''.join(c for c in i)) for i in perm(i)]
    return list

def perm_check(d):
    for i in d[1:]:
        if d[0] not in P(i):
            return False
    return True

p = Sieve(10000)
p = [i for i in p if i > 1000]
pairs = []
for i in p:
    print i
    for inc in range(1,10000-i):
        d = [i]
        new = i + inc
        while new in p: 
            d.append(new)
            new = new + inc
        if len(d) == 3 and perm_check(d):
            print d
            pairs.append(d)

        
print pairs
