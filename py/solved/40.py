#!/bin/sh

# P40.py
# ProjectEuler
#
# Created by joe yuan on 5/9/11.
# Copyright 2011 Classified. All rights reserved.
def solve():
    a = 1
    s = ''
    while len(s) < 1000000:
        a = a + 1
        s = ''.join(str(i) for i in range(10**a))

    p = 1
    for i in range(7):
        p = p*int(s[10**i])
        
    return p

from timer import time_function
print(time_function(solve))
