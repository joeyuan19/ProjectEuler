#!/bin/sh

# P48.py
# ProjectEuler
#
# Created by joe yuan on 3/29/11.
# Copyright 2011 Classified. All rights reserved.

s = 0
for i in range(1,1001):
    s = s + i**i
s = str(s)
print s[-10:]