#!/bin/sh

# P31.py
# ProjectEuler
#
# Created by joe yuan on 4/11/11.
# Copyright 2011 Classified. All rights reserved.


def solve():
    count = 1 # 1 for full set of each coin
    for b in range(3): # 100p
        _b = b*100
        for c in range((200-_b)//50 + 1): # 50p
            _c = _b + c*50
            for d in range((200-_c)//20+1): # 20p
                _d = _c + d*20
                for e in range((200-_d)//10+1): # 10p
                    _e = _d + e*10
                    for f in range((200-_e)//5+1): # 5p
                        _f = _e + f*5
                        for g in range((200-_f)//2+1): #2p
                            count += 1 # always less than 200 can fill rest with 1p
    return count
from timer import time_function
print(time_function(solve))
