#!/bin/sh

# P15.py
# ProjectEuler
#
# Created by joe yuan on 3/9/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.


#20 x 20 
#2(19 x 20)
#(19 x 19 + 18 x 20)
#18 x 20 = 18 x 19 + 17 x 20
#2(19 x 19 + 18 x 20)


p = ''
for i in range(20):
    p = p + 'r'

for i in range(20):
    p = p + 'd'
    


"""
explained nicely:

rrrrrrrrrrrrrrrrrrrrdddddddddddddddddddd

40! for total combinations

but you shouldnt account for permutations between r's and d's or 20! for each

40!/(20!*20!)
"""

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)

def solve():
    return factorial(40)/(factorial(20)**2)

from timer import time_function
print(time_function(solve))
