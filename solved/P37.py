#!/bin/sh

# P37.py
# ProjectEuler
#
# Created by joe yuan on 3/27/11.
# Copyright 2011 Classified. All rights reserved.

from math import *

global p
p = []
def prime(n,c=len(p)):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in p[:c]:
        if n%i == 0:
            return False
    return True

def trunc(n):
    s = str(n)
    for i in range(len(s)):
        if s[i:] != '':
            if not prime(int(s[i:]),len(p)-1):
                return False
        if s[:i+1] != '':
            if not prime(int(s[:i+1]),len(p)-1):
                return False
    return True

def main():
    t = 3
    tp = 0
    sum = 0
    while tp != 11:
        if prime(t):
            if len(str(t)) > 1:
                if trunc(t):
                    print t
                    sum = sum + t
                    tp = tp + 1
        t = t + 1
    print sum
            
main()
            