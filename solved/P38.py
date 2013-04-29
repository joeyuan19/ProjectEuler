#!/bin/sh

# P38.py
# ProjectEuler
#
# Created by joe yuan on 5/11/11.
# Copyright 2011 Classified. All rights reserved.

global k
k = [i for i in range(1,10)]

def c(n):
    s = str(n*1) + str(n*2)
    N = 3
    while len(s) < 9:
        s += str(n*N)
        if len(s) > 9:
            return False, s
        N += 1 
    x = [int(i) for i in s]
    x.sort()
    if x == k:
        return True,  s
    else:
        return False, s
        
        
n = 1
s = ''
most = 0
while len(str(n)) <= 5:
    print n
    u, s = c(n)
    if u:
        print u,s
        if int(s) > most:
            most = int(s)
    n += 1 
    
print most