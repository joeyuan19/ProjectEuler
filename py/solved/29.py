#!/bin/sh

# P29.PY
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.

def solve():
    l = []

    for a in range(2,101):
        for b in range(2,101):
            if a**b not in l:
                l.append(a**b)
            
    return len(l)

from timer import time_function
print(time_function(solve))
