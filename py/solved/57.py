from math import log10

def solve():
    P0 = 0
    P1 = 1
    N = 0
    for i in range(1000):
            n = P0 + P1
            d = P1
            if int(log10(n)) > int(log10(d)):
                    N += 1
            temp = P1
            P1 = 2*P1 + P0
            P0 = temp
    return N

from timer import time_function
print(time_function(solve))
