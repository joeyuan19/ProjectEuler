#!/bin/sh

# P54.py
# ProjectEuler
#
# Created by joe yuan on 7/28/11.
# Copyright 2011 Classified. All rights reserved.

def solve():
    s = []

    f = open("../files/poker.txt")
    for i in f:
        s.append(i)
        
    for i in range( len(s) ):
        t = ""
        for j in range( len(s[i]) ):
            if s[i][j] != " ":
                t += s[i][j]
        else:
            pass
        s[i] = t

    for i in s:
        print('"' + i[:-2] + '",')

from timer import time_function
print(time_function(solve))

