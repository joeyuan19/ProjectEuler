#!/bin/sh

# P6.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def solve():
    sum1 = 0
    sum2 = 0

    for i in range(0,101):
        sum1 = sum1 + i**2
        sum2 = sum2 + i
    sum2 = sum2**2
    return sum2 - sum1

from timer import time_function
print(time_function(solve))
