#!/bin/sh

# P96.py
# ProjectEuler
#
# Created by joe yuan on 3/21/11.
# Copyright 2011 Classified. All rights reserved.


import numpy as np




def rowbyrow():
    d = []
    for i in range(9):
        x = list(raw_input("Row " + str(i+1) + ":\n"))
        print(x)
        if len(x) != 9:
            print("Invalid number of entries, you need 9:")
            c = "n"
        else:
            c = raw_input("Is this correct? (y/n)\n")
        while c == "n":
            if c == "n":
                print("Please input the row again: ")
                x = list(raw_input("Row " + str(i+1) + ":\n"))
                print(x)
                c = raw_input("Is this correct? (y/n)\n")
        d.append(x)
    for k,i in enumerate(d):
        for j,c in enumerate(i):
                d[k][j] = int(c)
    return d

"""
def puzzprint(n):
    print('+ - - - + - - - + - - - +')
    for p in range(3):
        print('|'),
        for i in range(3):
            print n[p][i],
        print('|'),
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(3,6):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(6,9):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
"""
### useful functions

def ld(x, y):
    pos = [i for i in x if i not in y]
    return pos

### Transforms

def transpose(n):
    """Takes a square list-'Matrix' and gives back the transpose"""
    d = [[n[j][i] for j in range(len(n))] for i in range(len(n))]
    return d

def box(n):
    d = [[] for i in range(len(n))]
    m = 0
    for Q in range(len(n)):
        if 18 <= m < 27:
            if 24 <= m < 27:
                for i in range(6,9):
                    m = m + 1
                    for c in range(6,9):
                        d[Q].append(n[i][c])
            elif 21 <= m < 24:
                for i in range(3,6):
                    m = m + 1
                    for c in range(6,9):
                        d[Q].append(n[i][c])
            elif 18 <= m < 21:
                for i in range(3):
                    m = m + 1 
                    for c in range(6,9):
                        d[Q].append(n[i][c])
        elif 9 <= m < 18:
            if 15 <= m < 18:
                for i in range(6,9):
                    m = m + 1
                    for c in range(3,6):
                        d[Q].append(n[i][c])        
            elif 12 <= m < 15:
                for i in range(3,6):
                    m = m + 1
                    for c in range(3,6):
                        d[Q].append(n[i][c])
            elif 9 <= m < 12:
                for i in range(3):
                    m = m + 1
                    for c in range(3,6):
                        d[Q].append(n[i][c])
        elif m < 9:
            if 6 <= m < 9:
                for i in range(6,9):
                    m = m + 1
                    for c in range(3):
                        d[Q].append(n[i][c])
            elif 3 <= m < 6:
                for i in range(3,6):
                    m = m + 1
                    for c in range(3):
                            d[Q].append(n[i][c])
            elif m < 3:
                for i in range(3):
                    m = m + 1
                    for c in range(3):
                        d[Q].append(n[i][c])
            
    return d
    
def solved(n):
    # Checks if each position has been made into an integer
    d = 0
    for i in n:
        for c in i:
            if not type(c) == int:
                d = d + 1
    if d == 0:
        return True
    else:
        return False
    
def linecheck(n):
    for k,i in enumerate(n):
        for j,c in enumerate(i):
            if type(c) == list:
                n[k][j] = ld(c,i)
    return n

def single(puzzle):
    # Goes line by line finding variables then tests each possibility in a
    # list of variables then takes each possibility and checks to see
    # if that is the only variable spot in which that possibility appears.
    for line_index, line in enumerate(puzzle):
        for variable_index, variable1 in enumerate(line):
            if type(variable1) == list:
                for possibility in variable1:
                    count = 0
                    for variable2 in line:
                        if type(variable2) == list:
                            if possibility in variable2:
                                count = count + 1
                                if count > 1: break
                    if count == 1:
                        puzzle[line_index][variable_index] = possibility
                        break
    return puzzle

def confirm(n):
    # replaces the variables that have been knocked down to one possibility
    for k,i in enumerate(n):
        for j,c in enumerate(i):
            if type(c) == list:
                if len(c) == 1:
                    n[k][j] = int(c[0])
    return n

def step(n):
    # checks lines, eliminating variables and singularities
    n = linecheck(n)
    n = single(n)
    n = confirm(n)
    return n
    
def rc(n):
    # row column
    for w in range(2):
        n = transpose(n)
        n = step(n)
    return n
    
def boxxy(n):
    # box
    n = box(n)
    n = step(n)
    n = box(box(n))
    return n
    
def solve(n):
    n = rc(n)
    n = boxxy(n)
    n = confirm(n)
    return n
    
def var(n,t=0):
    # Gives coordinates for spot with the least number of variables.
    vc = []
    v = []
    for x1,line in enumerate(n):
        for x2,nums in enumerate(line):
            if type(nums) == list:
                vc.append([len(nums),[x1,x2]])
    vc.sort()
    m = vc[t]
    return m
        
def bruteforce1(n,xfs):
    # finds the variable with the lowest number of possiblities
    # cycles through the variables until the correct one has been found.
    m = var(n)
    for i in range(m[0]):
        n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
        u = False
        while not solved(n):
            n1 = n
            n = solve(n)
            if bfcondition(n):
                n = xfs[-1]
                m = var(n)
                break
            if n == n1:
                n2 = failsafe(n)
                xfs.append(n2)
                n, u = bruteforce2(n,xfs)
                if solved(n):
                    break
                m = var(n)
        if solved(n):
            break
    while not solved(n):
        if not bfcondition(n):
            break
        puzzprint(n)
        n1 = n
        n = solve(n)
        if n == n1:
            n2 = failsafe(n)
            xfs.append(n2)
            n = bruteforce1(n,xfs)
    return n
    
def bruteforce2(n,xfs):
    # finds the variable with the lowest number of possiblities
    # cycles through the variables until the correct one has been found.
    m = var(n)
    for i in range(m[0]):
        n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
        u = False
        while not solved(n):
            n1 = n
            n = solve(n)
            if bfcondition(n):
                n = xfs[-1]
                m = var(n)
                break
            if n == n1:
                n2 = failsafe(n)
                xfs.append(n2)
                n, u = bruteforce2(n,xfs)
                if solved(n):
                    break
            if bfcondition(n):
                n = xfs[-1]
                m = var(n)
                break
            if u:
                break
        if solved(n):
            break
    while not solved(n):
        if not bfcondition(n) or solved(n):
            break
        n1 = n
        n = solve(n)
        if n == n1:
            n2 = failsafe(n)
            xfs.append(n2)
            n = bruteforce1(n,xfs)
        puzzprint(n)
        
    if solved(n):
        return n, True
    elif not bfcondition(n):
        f = xfs[-1]
        xfs.pop()
        return f, False
    else:
        return n, True
        
def bfcondition(n):
    for i in n:
        for c in i:
            if c == []:
                return True
    for i in n:
        for c in i:
            if type(c) == int:
                if i.count(c) > 1:
                    return True
    for i in box(n):
        for c in i:
            if type(c) == int:
                if i.count(c) > 1:
                    return True
    for i in transpose(n):
        for c in i:
            if type(c) == int:
                if i.count(c) > 1:
                    return True
    return False

def failsafe(n):
    n1 = []
    for i in n:
        d = []
        for c in i:
            if type(c) == list:
                f = []
                for h in c:
                    f.append(h)
            else:
                f = c
            d.append(f)
        n1.append(d)
    return n1   

def Sudoku(n):
    xc = [i for i in range(1,10)]
    xgrid = []
    
    for i in range(9):
        dc = []
        for i in range(9):
            dc.append(xc)
        xgrid.append(dc)
    for i in range(9):
        for p,c in enumerate(n[i]):
            if c != 0:
                xgrid[i][p] = c


    while not solved(xgrid):
        xgrid1 = xgrid
        xgrid = solve(xgrid)
        if xgrid == xgrid1:
            xgrid2 = failsafe(xgrid)
            xfs = [xgrid2]
            xgrid = bruteforce1(xgrid,xfs)
    s = str(xgrid[0][0]) + str(xgrid[0][1]) + str(xgrid[0][2])
    return int(s), xgrid

"""
def puzzprint(n):
    print '+ - - - + - - - + - - - +'
    for p in range(3):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(3,6):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(6,9):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
"""
def euler96():
    f = open("../files/Sudoku.txt")
    p = []
    while 1:
        line = f.readline()
        if not line:
            break
        p.append(line[:9])

    puzzles = []
    d = []
    for i in p:
        if 'Grid' in i:
            puzzles.append(d)
            d = []
        else:
            d.append(i)
    puzzles.append(d)
    puzzles.pop(0)
    


    for j,i in enumerate(puzzles):
        x =[]
        for k,c in enumerate(i):
            d = []
            for h in c:
                d.append(int(h))
            x.append(d)
        puzzles[j] = x
    f = 1
    s = 0
    for i in puzzles:
        #print "##### ", f, " #####"
        c,x = Sudoku(i)
        #puzzprint(x)
        s = s + c
        f = f + 1
    return s

from timer import time_function
print(time_function(euler96))

