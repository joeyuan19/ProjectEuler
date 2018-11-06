from timer import time_function
#from scipy.optimize import curve_fit as cf
#import numpy as np

def BOP(k,s):
    # solve m*u = s
    L = len(s)
    m = [[n**i for i in range(L)]+[s[n-1]] for n in range(1,L+1)]
    m = echelon(m)
    u = [_m[-1] for _m in m]
    #print(u)
    return sum(_u*((k+1)**i) for i,_u in enumerate(u))


def echelon(m):
    L = len(m)
    for c in range(L):
        if m[c][c] != 1:
            m = multiply_row(m,c,1./m[c][c])
        for r in range(c+1,L):
            if m[r][c] != 0:
                m = add_scale_row(m,r,c,-m[r][c])
    for c in range(L-1,0,-1):
        for r in range(c-1,-1,-1):
            if m[r][c] != 0:
                m = add_scale_row(m,r,c,-m[r][c])
    return m

# 1. swap rows
# 2. multiply row by non-zero scaler
# 3. add a scaler multipl of one row to another
def swap_rows(m,i,j):
    t = m[i]
    m[i] = m[j]
    m[j] = t
    return m
   
def multiply_row(m,i,c):
    m[i] = [a*c for a in m[i]]
    return m

def add_scale_row(m,i,j,c):
    m[i] = [a+c*b for a,b in zip(m[i],m[j])]
    return m

def is_echelon(m):
    L = len(m)
    for i in range(L):
        for j in range(L):
            if i != j:
                if m[i][j] != 0:
                    return False
            else:
                if m[i][j] != 1:
                    return False
    return True

def u(n):
    return sum((-n)**i for i in range(11))
    #return n*n*n

def solve():
    N = 11
    seq = tuple(u(i) for i in range(1,N+1))
    return round(sum(BOP(k,seq[:k]) for k in range(1,N)))

print(time_function(solve))

