import sys
from math import sqrt

LIMIT = 2*10**3

def bruteforce(N):
    count = 0
    a = 1
    while True: 
        b = 1
        while b <= a:
            c = 1
            while c <= b:
                shortest = min(((a+b)**2 + c**2)**.5,((b+c)**2 + a**2)**.5,((c+a)**2 + b**2)**.5)
                if shortest == int(shortest):
                    count += 1
                    if count >= N:
                        return (a,count)
                        sys.exit()
                c += 1
            b += 1
        a += 1

def sum_of_squares(n):
    i = 1
    while i < n:
        j = i
        while j < n:
            if i*i + j*j == n:
                yield i,j
            j += 1
        i += 1

def one_minute(N):
    a = 1
    count = 0
    while True:
        bc = 1
        while bc <= a:
            l = sqrt(a*a+bc*bc)
            if intcheck(l):
                count += bc//2
                if count >= N:
                    return a
            bc += 2
        a += 1

def intcheck(x):
    return x == x//1

def fast(M):
    I = 0
    for a in range(1,M+1):
        for b in range(a,M+1):
            for c in range(b,M+1):
                if intcheck((c**2 + (a+b)**2)**.5):
                    I += 1
    return I

# d^2 = c^2 + (a+b)^2
# d^2 - c^2 = (a+b)^2
# d = c + n, n = 1,2,3,...
# (c+n)^2 = c^2 + (a+b)^2
# c^2 + 2cn + n^2 = c^2 + (a+b)^2
# 2cn + n^2 = (a+b)^2
# at min: b = sqrt(2c + 1) - a


# ab | a + b                      | M = 2 | 3
#  2 | 1 + 1                      | 1     | 1
#  3 | 1 + 2                      | 1     | 1
#  4 | 1 + 3, 2 + 2               | 1     | 2
#  5 | 1 + 4, 2 + 3               | 0     | 1
#  6 | 1 + 5, 2 + 4, 3 + 3        | 0     |
#  7 | 1 + 6, 2 + 5, 3 + 4        | 0     |
#  8 | 1 + 7, 2 + 6, 3 + 5, 4 + 4 | 0     |
#  9 | 1 + 8, 2 + 7, 3 + 6, 4 + 4 | 0     |

# number of sums per integer = i//2
# number of sums per integer whose maximal summation is M+M of which neither value can exceed M is
# M = 4
# ab = 8 only 1 sum is valid 4+4      | (ab - M)//2 = 1
# ab = 7 only 1 sum is valid 3+4      | ab - M = 1
# ab = 6 only 2 sum is valid 3+3, 2+4 | ab - M = 2
# ab = 5 only 2 sum is valid 2+3, 1+4 | ab - M = 3
# ab = 4 only 2 sum is valid 2+2, 1+3
# ab = 3 only 1 sum is valid 1+2
# ab = 2 only 1 sum is valid 1+1
#

# For ab > M number of sums is equal to 


def sfast(N):
    I = 0
    M = 1
    while True:
        for a in range(1,M+1):
            for b in range(a,M+1):
                d = (M**2 + (a+b)**2)**.5
                if d == int(d):
                    I += 1
                if I > N:
                    return M,I
        M += 1

def sfast2(N):
    I = 0
    M = 1
    while True:
        for a in range(1,M+1):
            for b in range(max(a,int(sqrt(2*M+1))),M+1):
                d = (M**2 + (a+b)**2)**.5
                if d == int(d):
                    I += 1
                if I > N:
                    return M,I
        M += 1


# c >= b >= a
# d^2 = c^2 + (a+b)^2
# d > c
# d^2 - c^2 = (a+b)^2
# p = d^2 - c^2
# 4 <= p <= M^2
# only need to check squres
# d = c + m, m = 1, 2, 3, ..., 2M

def sfast3(N):
    I = 0
    M = 1
    while True:
        for ab in range(2,M+1):
            d = (M**2 + ab**2)**.5
            if d == int(d):
                I += ab//2
            if I > N:
                return M,I
        for ab in range(M+2,2*M+1):
            d = (M**2 + ab**2)**.5
            if d == int(d):
                #I += ab//2 - ab + 1 + M
                I += M - ab//2 + 1
            if I > N:
                return M,I
        M += 1

def time_function(f,*args):
    import time
    t = time.time()
    r = f(*args)
    return (r,time.time() - t)

N = 1e6
print(time_function(sfast3,N))

