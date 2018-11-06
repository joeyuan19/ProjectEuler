from prime import sieve

"""
OEIS series A00872

Given by a(n)

"""

def count(n):
    N = n
    s = sieve(N)
    solution = [1]+[0]*N
    for p in s:
        for j in range(p,N+1):
            solution[j] += solution[j-p]
    return solution[-1]


def solve():
    for n in range(2,100):
        if count(n) > 5000:
            return n

from timer import time_function
print(time_function(solve))
