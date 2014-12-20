#!/bin/sh

# P10.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def prime(f):
    prime = [2]
    for i in range(3,f,2):###<----modify to range(3,f) for primes up to f
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u:
            print i
            prime.append(i)
    return prime

p = prime(2000000)

sum = 0
for i in p:
    sum = sum + i
print sum
