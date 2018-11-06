#!/bin/sh

# P36.py
# ProjectEuler
#
# Created by joe yuan on 3/14/11.
# Copyright 2011 Classified. All rights reserved.



def binary(n):
    if n == 0:
        return 0
    bi_n = ''
    exp = 0
    while 2**exp <= n:
        exp += 1
    exp -= 1
    while exp >= 0:
        c = 2**exp
        if c <= n:
            bi_n += '1'
            n = n - c
        else:
            bi_n += '0'
        exp -= 1
    return int(bi_n)
    
def palindrome_check(n):
    s = str(n)
    for i in range(len(s)//2 + 1):
        if s[i] != s[-(i+1)]:
            return False
    return True

def base_check(n):
    #if len(str(n)) == 1:
    #    return False
    if palindrome_check(n) and palindrome_check(binary(n)):
        return True
    else:
        return False
        
def main(N=1000000):
    s = 0
    for i in range(N):
        if base_check(i):
            #print i, binary(i), base_check
            s += i
        else:
            pass
    return s
    
from timer import time_function
print(time_function(main))


