"""
Almost equilateral triangles
Problem 94

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).


A = base*height/2
if A is integer, then base*height is even:
b|h|bh
------
o|o|o
o|e|e
e|o|e
e|e|e

"""

import time
from timer import time_function
from math import sqrt

def bruteforce(LIMIT_P):
    LIMIT_S = (LIMIT_P + 1)/3
    LIMIT_H = int(sqrt(3*LIMIT_S**2/4 + LIMIT_S/2 - 1/4))+1
    P = 0
    for ds in (-1,1):
        for h in range(1,LIMIT_H,2):
            s = (ds + 2*sqrt(1 + 3*h**2))/3  # 1 + 3*h**2 = even if h is odd, ... = odd if h is even 
            if s%2 == 0:
                P += 3*s + ds
        for h in range(2,LIMIT_H,2):
            s = (ds + 2*sqrt(1 + 3*h**2))/3
            if s == s//1:
                P += 3*s + ds
    return P

def odd_s(LIMIT_P):
    LIMIT_S = (LIMIT_P+1)//3 + 1
    P = 0
    for ds in (-1,1):
        for s in range(1,LIMIT_S,2):
            x = sqrt(s*s - ((s+ds)/2)**2)
            if x//1 == x:
                P += 3*s + ds
    return P

def by_h(LIMIT_P):
    LIMIT_S = (LIMIT_P+1)//3 + 1
    LIMIT_H = int(.5*sqrt(3*LIMIT_S*LIMIT_S + 2*LIMIT_S - 1))+1 
    LIMIT_S = int((1 + sqrt(1 + 3*LIMIT_H*LIMIT_H))/3)+1
    h,s = 1,-1
    P = 0
    while True:
        for ds in (-1,1):
            s = (ds + 2*sqrt(1+3*h*h))/3
            if s >= LIMIT_S:
                return P
            elif s//1 == s:
                P += 3*s + ds
        h += 1

def by_h2(LIMIT_P):
    LIMIT_S = (LIMIT_P+1)//3 + 1
    #LIMIT_H = int(.5*sqrt(3*LIMIT_S*LIMIT_S + 2*LIMIT_S - 1))+1 
    #LIMIT_S = int((1 + sqrt(1 + 3*LIMIT_H*LIMIT_H))/3)+1
    LIMIT_S3 = LIMIT_S//3+1 
    h,s3 = 1,3
    P = 0
    while s3 < LIMIT_S3:
        for ds in (-1,1):
            h = sqrt((s3*s3 - 2*s3*ds - 3)/12)
            if h//1 == h:
                P += s3 + ds
        s3 += 6
    return P

def oneminute(N):
    P = 0 
    LIMIT_S = (N+1)//3 + 1
    LIMIT_D = int(sqrt(3*LIMIT_S*LIMIT_S + 2*LIMIT_S - 1))+1
    for ds in (-1,1):
        for d in range(2,LIMIT_D,2):
            s = (sqrt(4+3*d*d) + ds)/3
            if s//1 == s:
                P += 3*s + ds
    return P


#print('odd_s')
#for N in [10**i for i in range(8)]:
#    print(time_function(odd_s,N))

#print('by_h')
#for N in [10**i for i in range(8)]:
#    print(time_function(by_h,N))


# Rearrange into pell x^2 - 3*y^2 = 1
# solutions exist where s = (2*y +- 1)/3 is an integer


def continued_frac_sqrt_3():
    n = 1
    d = 1
    yield n,d
    I = 0
    alt = True
    while True:
        n,d = 1,1 if alt else 2
        _alt = alt 
        for i in range(I):
            n,d = d,(2 if _alt else 1)*d+n
            _alt = not _alt
        yield d+n,d
        I += 1
        alt = not alt

def pell(x,y,n,sign):
    return x*x - n*y*y == sign

def fundamental_solution(n,sign):
    for num,denom in continued_frac_sqrt_3():
        if pell(num,denom,n,sign):
            return num,denom

def pell_solutions(n,sign):
    x1,y1 = fundamental_solution(n,sign)
    _x,_y = x1,y1
    while True:
        _x,_y = x1*_x + n*y1*_y, x1*_y + y1*_x
        yield _x,_y

def solve():
    P = 0
    for x,y in pell_solutions(3,1):
        for ds in (-1,1):
            s = (2*x + ds)/3
            if s//1 == s:
                p = 3*s + ds
                if p > 1e9:
                    return P
                P += p

print(time_function(solve))


