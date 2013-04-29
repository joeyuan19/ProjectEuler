#!/bin/sh

# P25.py
# ProjectEuler
#
# Created by joe yuan on 3/11/11.
# Copyright 2011 Classified. All rights reserved.



def len_num(f):
    n = str(f)
    return len(n)
    

a = 1
b = 1
c = a + b
t = 3 #indicates which fibo term your at
print a
print b
while len_num(c) < 1000:
    a = b
    b = c
    c = b + a
    t = t + 1
print t

### try: 4782