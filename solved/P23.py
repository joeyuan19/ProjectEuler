#!/bin/sh

# P23.py
# ProjectEuler
#
# Created by joe yuan on 3/11/11.
# Copyright 2011 Classified. All rights reserved.


def factor(f):
    factor = []
    sum = 0
    for i in range(1,f/2 + 1):###<----modify to range(3,f) for primes up to f
        if f%i == 0: 
            sum = sum + i
    if sum > f:
        return True
    else:
        return False

def abundance_list(f):
    ab = []
    for i in range(f+1):
        if factor(i):
           ab.append(i)
    return ab
    
    
def ab_sum_test(f,ab):
    for c in ab:
        if (i-c) > 0:
            if (i - c) in ab:
                return True
        else:
            return False
    return False


ab = abundance_list(28123)

sum = 0
for i in range(28124):
    if not ab_sum_test(i,ab):
        print i
        sum = sum + i
print sum

### Try 4179871 
### last output was: 20161 why would limit be 28000 if the last one is that????





