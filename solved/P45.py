#!/bin/sh

# P45.py
# ProjectEuler
#
# Created by joe yuan on 4/11/11.
# Copyright 2011 Classified. All rights reserved.


def t(n):
    return n*(n + 1)/2

def p(n):
    return n*(3*n - 1)/2
    
def h(n):
    return n*(2*n - 1)
    
    
def equality(h,index):
    i = index
    while 1:
        pent = p(i)
        if pent > h:    
            return False
        elif pent == h:
            break
        i = i + 1
    i = index
    while 1:
        tri = t(i)
        if tri > h:
            return False
        elif tri == h:
            break
        i = i + 1
    return True
        
        
index = 144
hex = h(index)

while not equality(hex,index):
    index += 1
    hex = h(index)
    
print index, hex


"""
  
  
  
  
  
  
  
  
  
  
  

def t_ck(n,index,t_index):
    for i in range(index,t_index):
        if n == t(i):
            return True
        elif p(i) > n:
            break
    return False

def p_ck(n,index,t_index):
    for i in range(index,t_index):
        if n == p(i):
            return True
        elif p(i) > n:
            break
    return False

def h_ck(n,index,t_index):
    for i in range(index,t_index):
        if n == h(i):
            return True
        elif h(i) > n:
            break
    return False

t_index = 285
p_index = 165
h_index = 143
n = h(h_index)

count = 0
while 1:
    if p_ck(n,p_index,h_index) and t_ck(n,t_index,h_index):
        count = count + 1
        if t == 2:
            break
        t_index = t_index + 1
        n = t(t_index)
    else:
        t_index = t_index + 1
        n = t(t_index)

print n
"""