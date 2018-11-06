# b*(b-1) / t*(t-1)  = 1/2
# t = r + b
# 2*b*(b-1) = t*(t-1)
# 2*(b**2 - b) = t**2 - t
# 2*(b**2 - b) - t**2 + t = 0
# 2*[ (b - 1/2)**2 - 1/4] - [(t - 1/2)**2 - 1/4] = 0
# 2*(b - 1/2)**2 - 1/2 - (t - 1/2)**2 + 1/4 = 0
# 2*(b - 1/2)**2 - (t - 1/2)**2 = 1/4
# 8*(b - 1/2)**2 - 4*(t - 1/2)**2 = 1
# 2*[2*(b - 1/2)]**2 - [2*(t - 1/2)]**2 = 1
# 2*[2*b - 1]**2 - [2*t - 1]**2 = 1
# [2*t - 1]**2 - 2*[2*b - 1]**2 = -1
# x = 2*t - 1
# y = 2*b - 1
# x**2 - 2*y**2 = 1
# t = (x + 1)/2
# b = (y + 1)/2
# Pell Eq (n=2)
# fundamental
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))
# hi/ki first to satisfy above eq
# x_k+1 = x1*x_k + n*y1*y_k
# y_k+1 = x1*y_k + y1*x_k

from timer import time_function
from math import sqrt

def continued_frac_sqrt_2():
    n = 1
    d = 1
    yield n,d
    I = 0
    while True:
        n,d = 1,2
        for i in range(I):
            n,d = d,2*d+n
        yield d+n,d
        I += 1

def pell(x,y):
    return x*x - 2*y*y == -1

def fundamental_solution():
    for n,d in continued_frac_sqrt_2():
        if pell(n,d):
            return n,d

def pell_solutions():
    x1,y1 = fundamental_solution()
    _x,_y = x1,y1
    while True:
        _x,_y = x1*_x + 2*y1*_y, x1*_y + y1*_x
        yield _x,_y

# if t > 10^12
def f4(N):
    for x,y in pell_solutions():
        b = (y + 1)/2
        t = (x + 1)/2
        if t > N and t//1 == t and b//1 == b:
            return b,t

N = 1e12
print(time_function(f4,N))

# Brute force attempts

def f(N):
    T = int(N)
    while True:
        for r in range(1,T):
            if 2*r*(r-1) == T*(T-1):
                print(r,'/',T,' ',r-1,'/',T-1)
        T += 1

def f1(N):
    T = int(N)
    while True:
        P = T*(T+1)/2
        p = int(sqrt(P))
        if p*(p+1) == P:
            return p+1
        T += 1

def f2(N):
    T = int(N)
    while True:
        x = 1 + sqrt(1 + 2*(T*T - T)) 
        if x%2 == 0:
            return x/2
        T += 1

def f3(N):
    p = N/2
    p2 = N
    while True:
        b = int(sqrt(p))
        t = int(sqrt(p2))
        if p == _p*(_p+1) and p2 == _p2*(_p2+1):
            return _p+1
        p += 1
        p2 = 2*p
