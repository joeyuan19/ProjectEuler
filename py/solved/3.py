#!/bin/sh

# P3.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

import numpy as np

def prime(f):
    prime = [2]
    for i in range(3,int(f**.5)):
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u and f%i == 0: 
            prime.append(i)
    return prime
    

n = 600851475143
print np.sqrt(n)
f = prime(n)
#primes = [2]
#for i in range(3,int(np.sqrt(n))):
 #   for c in primes:
  #      if i%c == 0:
   #         u = False
    #        break
     #   u = True
#    if u:
 #       primes.append(i)
  #      if n%i == 0:
   #         f = i
    #if i%1000 == 0:
     #   print f, primes
                


print f[-1]