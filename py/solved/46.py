#!/bin/sh

# P46.py
# ProjectEuler
#
# Created by joe yuan on 3/29/11.
# Copyright 2011 Classified. All rights reserved.

from numpy import sqrt

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

def composite_check(n):
    if n > 0 and n%2 != 0:
        if not prime(n):
            return True
    else:
        return False

def sieve_odd_composite(N=1000):
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
    pr = [(j+1) for j,i in enumerate(x) if i == 0]
    oddcomp = [(j+1) for j,i in enumerate(x) if i != 0 and (j+1)%2 == 1]
    return oddcomp, pr



'''
smallest composite that cannot be written:

x = a + 2 (b^2) where a is prime

'''
def solve():
    N = 10000
    inc = 1
    found = False
    while not found:
        
        oddcomp, pr = sieve_odd_composite(N*inc)

        for n in oddcomp:
            if n == 1:
                pass
            else:
                for a in pr:
                    if a > n:
                        s = True
                        break
                    b = 1
                    while 1:
                        if n < a + 2*(b**2):
                            u = True
                            break
                        elif n == a + 2*(b**2):
                            u = False
                            break 
                        b += 1
                    if not u:
                        s = False
                        break
                if s:
                    return n
                    found = True
                    break
                    
                    
                    
        #print n,"on to the next one"
        inc += 1

from timer import time_function
print(time_function(solve))
