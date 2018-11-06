#!/bin/sh

# p7.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


def prime(f):
    prime = [2]
    #for i in range(3,int(f**.5)): #<----prime factors
    #for i in range(3,int(f**.5)) #<----modified for primes up to f
    y = 1003
    while len(prime) != f: #<----n number of primes
        for i in range(y-1000,y): #<---- indent everything below 
            #if i%1000 == 0:
            #    print(i, len(prime))
            for c in prime:
                if i%c == 0:
                    u = False
                    break
                u = True
            if u: 
                prime.append(i)
            if len(prime) == f:
                break
        y = y + 1000
    return prime

def solve():
    f = 10001
    p = prime(f)
    return p[-1]

from timer import time_function
print(time_function(solve))
