#!/bin/sh

# primecheck.py
# ProjectEuler
#
# Created by joe yuan on 4/26/11.
# Copyright 2011 Classified. All rights reserved.


def prime(f):
    if f < 2:
        print f, "is less than 2 and 2 is the smallest prime number"
        return []
    prime = [2]
    for i in range(3,f,2):
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u: 
            prime.append(i)
    return prime
    
p = prime(10000)

for i in p:
    if i > 3:
        c = (i**2)%12 + 2
        print c

