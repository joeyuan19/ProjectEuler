#!/bin/sh

# P24.py
# ProjectEuler
#
# Created by joe yuan on 3/11/11.
# Copyright 2011 Classified. All rights reserved.

from math import factorial as f
from itertools import *

def list_str(a):
    if type(a) != list:
        a = list(str(a))
    return a

def solve():
    a = list_str("123")
    b = []
    for i in permutations('0123456789'):
        b.append(i)
        
    return int(''.join(b[999999]))

from timer import time_function
print(time_function(solve)) 
        
