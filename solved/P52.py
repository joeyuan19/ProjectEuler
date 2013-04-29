#!/bin/sh

# P52.py
# ProjectEuler
#
# Created by joe yuan on 3/29/11.
# Copyright 2011 Classified. All rights reserved.


def p6(n,n2,n3,n4,n5,n6):
    s = list(str(n))
    s2 = list(str(n2))
    s3 = list(str(n3))
    s4 = list(str(n4))
    s5 = list(str(n5))
    s6 = list(str(n6))
    print s, s2
    if ld(s,s2):
        print s, s2
        if ld(s,s3):
            if ld(s,s4):    
                if ld(s,s5):
                    if ld(s,s6):
                        return True
    return False

def p2(n,n2):
    s = list(str(n))
    s2 = list(str(n2))
    print s,s2
    if ld(s,s2):
        return True
    return False

def ld(x1,y1):
    x = [i for i in x1]
    y = [i for i in y1]
    pos = []
    if len(x) != len(y):
        return False
    while len(x) > 0:
        for i in x:
            if i in y:
                x.pop(x.index(i))
                y.pop(y.index(i))
                u = True
            else:
                u = False
                return False
        if not u:
            return False
    return True

i = 10
while not p6(i,i*2,i*3,i*4,i*5,i*6):
    i = i + 1
print i