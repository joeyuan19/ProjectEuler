from timer import time_function
#!/bin/sh

# P1.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

"""
# Original Solution commented out 4/4/17
sum = 0
for i in range(1001):
    if i%3 == 0 or i%5 == 0:
        sum = sum + i
        print i
print sum
"""
def f(N):
    return sum(i for i in range(1,N) if (i%3 == 0 or i%5 == 0))
print(time_function(f,1000)) 
