#!/bin/sh

# P28.py
# ProjectEuler
#
# Created by joe yuan on 5/11/11.
# Copyright 2011 Classified. All rights reserved.


n = 1
step = 2
t = 0
sum = 0
while 1:
    sum += n
    if n >= 1001**2:
        break
    n += step
    t += 1
    if t%4 == 0:
        step += 2
print sum
