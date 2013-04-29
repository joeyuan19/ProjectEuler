#!/bin/sh

# P66.py
# ProjectEuler
#
# Created by joe yuan on 3/29/12.
# Copyright 2012 Classified. All rights reserved.

from math import sqrt

def dio(x, d):
    return sqrt((x*x - 1)/d)

def dioCheck(x,y,d):
    return x*x - d*y*y == 1

def intCheck(x):
    return x == int(x)

xMax = 0
dMax = 0

N = 62
solnFound = False
for d in range(N):
    if sqrt(d) != int(sqrt(d)):
        y = 1
        x = 1

        solnFound = False
        while not solnFound:
            while y*y > (x*x - 1)/d:
                x += 1
            if y*y == (x*x - 1)/d:
                solnFound = True
            else:
                y += 1
        """
        while not intCheck(x):
            y += 1
            x = dio(y,d)
            itr += 1
            print str(x) + "^2 - (" + str(d) + ")" +  str(y) + "^2 = 1"  
            if itr > 10000:
                break
        if itr > 10000:
            print "broken"
            break
        print "SOLN FOUND####################"
        """
        
        if x > xMax:
            print d
            xMax = x
            dMax = d
    
print "d at x-maximum =", dMax