#!/bin/sh

# perm.py
# ProjectEuler
#
# Created by joe yuan on 3/15/11.
# Copyright 2011 Classified. All rights reserved.


def perm(n):
    n1 = str(n)
    p =[]
    for i in range(len(n1)):
        n1 = (''.join(i for i in n1[1:] + n1[0]))
        p.append(int(n1))
    return p
    
print perm(123)