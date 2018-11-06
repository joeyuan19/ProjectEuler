#!/bin/sh

# P79.py
# ProjectEuler
#
# Created by joe yuan on 10/1/11.
# Copyright 2011 Classified. All rights reserved.


def solve():
    with open("keylog.txt") as f:
        p = [line for line in f]
    key = [[],[],[]]
    for c in p:
        for i in range(3):
            key[i].append(int(c[i]))
    
    key2 = [[i for i in key[0] if i not in key[1]],
            [i for i in key[1] if i not in key[0]],
            [i for i in key[1] if i not in key[2]],
            [i for i in key[2] if i not in key[1]]]
    key3 = [[i for i in key[0] if i in key[1]],
            [i for i in key[1] if i in key[0]],
            [i for i in key[1] if i in key[2]],
            [i for i in key[2] if i in key[1]]]

    for i in key3:
        f = []
        for j in i:
            if j not in f: f.append(j)
        f.sort()
        print(f)
    for i in key2:
        print(i)
    for i in key3:
        print(i)

from timer import time_function
print(time_function(solve))
