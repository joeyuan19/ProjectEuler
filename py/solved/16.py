#!/bin/sh

# P16.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def solve():
    e = 2**1000
    s = 0
    for i in str(e):
        s =  s + int(i)
    return s

from timer import time_function
print(time_function(solve))
