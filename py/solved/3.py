from timer import time_function
#!/bin/sh

# P3.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

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
    
def solve():
    n = 600851475143
    f = prime(n)
    return f[-1]

print(time_function(solve))
