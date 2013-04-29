#!/bin/sh

# P2.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def evenfib(n):
    """Finds the sum of the even numbers in fibonacci seq up to n"""
    f = [0,1,2]
    fnew = 0
    while fnew < n:
        fnew = f[-1] + f[-2]
        f.append(fnew)
    if f[-1] > n:
        f.pop()
    sum = 0
    for i in f:
        if i%2 == 0:
            sum = sum + i
    return sum
print evenfib(4000000)