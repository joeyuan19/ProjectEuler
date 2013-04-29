#!/bin/sh

# P352.py
# ProjectEuler
#
# Created by joe yuan on 10/6/11.
# Copyright 2011 Classified. All rights reserved.

def SUM(T,p):
    s = 0
    for i in range(1,int(T)+1):
        s += (1./(2**i))*((T/i) - 1)*( 1 - ((1-p)**(T/i)))
    return s
"""
def P(T,n,p):
    #SP = (P(initial test) = 1 + P(subsequent tests) = P(chance of infection))
    SP = ( 1 + SUM(T,n,p))*n - n*16
    #SP = n + T*(p**(T/n))
    return SP
"""
def Sum(T,p):
    s = 0
    for i in range(T,0,-1):
        print i
def P(t,p):
    SP = ( 1 + SUM(T,p))
    return SP
T = 25.0
p = 0.02
for i in range(1,int(T+1)):
    #print P(T,float(i),p)
    #print 1 - ((1-p)**(T/i))
    #Sum(T,p)
    print P(T,p)
"""
worst case first depth search method
     g1
    /  \
  g2    g5
  /\    /\
 g3 g4 g6 g7
"""