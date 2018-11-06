#!/bin/sh

# P5.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

def solve():
    t = [i for i in range(11,21)]
    n = False
    y = 20020
    while not n:
        for i in range(y-20000,y,20):
            for c in t:
                if i%c != 0:
                    u = False
                    break
                u = True
            if u:
                f = i
                n = True
                break
        if u:
            n = True
            break
        y = y + 20000
                    
    return f

from timer import time_function
print(time_function(solve))
