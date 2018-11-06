#!/bin/sh

# P35.py
# ProjectEuler
#
# Created by joe yuan on 3/13/11.
# Copyright 2011 Classified. All rights reserved.


from math import sqrt
from itertools import *

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(sqrt(n)) + 1,2):
        if n%i == 0:
            return False
    return True


def prime2(n):
    global p
    p = [2]
    for i in range(3,n,2):
        #print i
        for c in p:
            if i%c == 0:
                u = False
                break
            u = True
        if u: 
            p.append(i)
    return p

#def perm(n):
 #   l = []
  #  for i in permutations(str(n)):
   #     l.append(i)
    #for h,i in enumerate(l):
     #   a = int(''.join(c for c in i))
      #  l[h] = a
#    return l

def perm(n):
    n1 = str(n)
    p =[]
    for i in range(len(n1)):
        n1 = (''.join(i for i in n1[1:] + n1[0]))
        p.append(int(n1))
    return p

def f(l):
    s = 0
    for i in l:
        if prime(i):
            s = s + 1
        else:
            return False
    if s == len(l):
        return True
    else:
        return False
            
def pm_ck(n=1000000):
    s = 0
    for i in range(n):
        if prime(i):
            if f(perm(i)):
                #print i
                s = s + 1
    return s

def solve():
    return pm_ck()

from timer import time_function
print(time_function(solve))
#x = input("n = ")
#if type(x) == int:
#    print pm_ck(x)
#else:
#    print pm_ck()
        
        
##### 55 #####
