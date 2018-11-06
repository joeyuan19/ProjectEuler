#!/bin/sh

# P18.py
# ProjectEuler
#
# Created by joe yuan on 3/12/11.
# Copyright 2011 Classified. All rights reserved.

x = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17,57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27,29,48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69,87,40,31],
[ 4, 62, 98, 27, 23,  9,  7, 98, 73, 93, 38,53, 6, 4,23]
]


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

from timer import time_function
print(time_function(triangle_sum,x))

