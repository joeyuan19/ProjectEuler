#!/bin/sh

# P14.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

x = []
for i in range(1000000,0,-1):
    print i
    d = []
    d.append(i)
    c = i
    while c != 1:
        if c%2 == 0:
            c = c/2
        else:
            c = 3*c + 1
        d.append(c)
    x.append([len(d),d[0]])
x.sort()
print x[-1]

