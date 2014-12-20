#!/bin/sh

# P1.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


sum = 0
for i in range(1001):
    if i%3 == 0 or i%5 == 0:
        sum = sum + i
        print i
print sum