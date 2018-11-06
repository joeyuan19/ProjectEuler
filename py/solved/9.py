#!/bin/sh

# P9.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def solve():
    for c in range(1,1000):
        for b in range(1,c):
            for a in range(1,b):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a*b*c
from timer import time_function
print(time_function(solve))
