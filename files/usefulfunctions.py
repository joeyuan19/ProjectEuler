#!/bin/sh

# usefulfunctions.py
# ProjectEuler
#
# Created by joe yuan on 5/10/11.
# Copyright 2011 Classified. All rights reserved.


def triangle_sum(x):
    y = []
    for i,c in enumerate(x):
        dummy_row = []
        if len(c) > 1: 
            for j,p in enumerate(c):
                if j != 0 and j != (len(c) - 1):
                    a = p + y[-1][j]
                    b = p + y[-1][j-1]
                    if a > b:
                        dummy_row.append(a)
                    else:
                        dummy_row.append(b)
                elif j == 0:
                    dummy_row.append(p + y[-1][j])
                else:
                    dummy_row.append(p + y[-1][-1])
            y.append(dummy_row)
        else:
            y.append(x[i])
    return max(y[-1])
    
def lc(x,y):
    for i in x:
        if i not in y:
            return False