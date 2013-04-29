#!/bin/sh

# P63.py
# ProjectEuler
#
# Created by joe yuan on 10/1/11.
# Copyright 2011 Classified. All rights reserved.
"""
from math import log10
 
s = 0
for n in range(1,10):
  s += int( 1 / (1-log10(n)) )
 
print "Answer to PE63 =", s
"""
i = 2
s = 0
while 1:
    n = len(str(i))
    c = 2
    g = c**n
    if g > i:
        print "###",s,"###"
        break
    while g <= i:
        if g == i:
            s += 1
            print s
            break
        else:
            c += 1
            g = c**n
    i += 1
    
    
