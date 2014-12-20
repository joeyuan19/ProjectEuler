#!/bin/sh

# P34.py
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.

from math import factorial as f

def factorial_sum(n):
    if type(n) != list:
        n = list(str(n))
    for j,i in enumerate(n):
        n[j] = int(i)
    sum = 0
    for i in n:
        sum = sum + f(i)
    return sum


s = 0
for i in range(10,9999999):
    if factorial_sum(i) == i:
        s = s + i
        
print s