#!/bin/sh

# P12.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


## FULL PRIME FACTORIZATION OF A NUMBER with exponent count  in form [primefactor,exponent] 
def primefactor(f):
    factors = [2]
    for i in range(3,int(f**.5),2):
        for c in factors:
            if i%c == 0:
                u = False
                break
            u = True
        if u and f%i == 0: 
            factors.append(i)
    pf = []
    for c in factors:
        g = 0
        for i in range(1,10000):
            if f%(c**i) != 0:
                pf.append([c,g])
                break
            else:
                g = i
    if pf[0][1] == 0:
        pf.pop(0)
    return pf

def ndiv(f):
    pf = primefactor(f)
    t = 1
    for i in pf:
        t = t*(i[1]+1)
    return t

def solve():
    i = 1
    tri = i
    while ndiv(tri)<500:
        i = i + 1
        tri = tri + i
    return tri
 
### try 76576500
from timer import time_function
print(time_function(solve))
















#um = 0
#c = 1
#n = 0
#while c < 500:
 #   c = 1
  #  sum = sum + n
   # for i in range(1,(sum+1)/2 + 1):
    #    if sum%i == 0:
     #       c = c + 1
      #  if c>500:
       #     break
    #n = n + 1
    #if sum%1000000 == 0:
     #   print sum
    
#print sum
            
    
