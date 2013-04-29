#!/bin/sh

# P9.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


for c in range(1000):
    for b in range(c):
        for a in range(b):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print a,b,c
                    print a*b*c