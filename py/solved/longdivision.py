#!/bin/sh

# longdivision.py
# ProjectEuler
#
# Created by joe yuan on 4/26/11.
# Copyright 2011 Classified. All rights reserved.

print "divides numbers of the form a/b"
a = int(raw_input("input a: "))
b = int(raw_input("input b: "))

def div(a,b):
    return a/b, a%b


print str(a) + '/' + str(b), "=",

a, R = div(a,b)

print str(a), ".",

while R != 0:
    if R < b:
        R = R*10
    a, R = div(R,b)
    print a,

    