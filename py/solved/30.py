#!/bin/sh

# P30.py
# ProjectEuler
#
# Created by joe yuan on 3/27/11.
# Copyright 2011 Classified. All rights reserved.


def fifth(n):
    s = str(n)
    sum = 0
    for i in s:
        sum = sum + int(i)**5
    if sum == n:
        return True
    else:
        return False

def main():
    sum = 0
    for i in range(10,100000000):
        if fifth(i):
            print i
            sum = sum + i
    print '\n',sum

main()