#!/bin/sh

# 76.py
# ProjectEuler
#
# Created by joe yuan on 10/3/11.
# Copyright 2011 Classified. All rights reserved.

def spread(S,L):
    tmp = [0]*L
    for i in range(S):
        tmp[i%L] += 1
    return tmp

def count(li):
    if len(li) == 2:
        print li
        return sum(li)/2
    else:
        if li[0] < li[1]:
            li = [sum(li)-len(li)+2]+[1]*(len(li)-2)
            return count(li)
        else:
            print li
            li[0] -= 1
            li[1] += 1
            return count(li)

N = 5
for N in range(2,N+1):
    print N,count([1]*N)


