#!/bin/sh

# P26.py
# ProjectEuler
#
# Created by joe yuan on 5/17/11.
# Copyright 2011 Classified. All rights reserved.

def div(a,b):
    return a/b, a%b

def repeat(s):
    for i in range(1,len(s)):
        c = s[:i]
        most = 0
        for j in range(len(s)/i):
            if c != s[j:j+i]:
                len(c)
                break
#print str(a) + '/' + str(b), "=",
a = 1
for b in range(1,1000):
    a = 1
    a, R = div(a,b)
    #print str(a), ".",
    x = str(a) + '.'
    while R != 0:
        if R < b:
            R = R*10
        a, R = div(R,b)
        x = x + str(a)
        if len(x) > 100:
            break
    repeat(x[2:])
    print "1","/",b, x
    