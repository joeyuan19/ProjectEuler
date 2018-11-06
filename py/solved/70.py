from totient import totients
import time

def solve():
    N = 10**7
    L = N+1
    t = totients(N)
    return min((float(i)/t[i],i) for i in range(2,L) if sorted(str(i)) == sorted(str(t[i])))

from timer import time_function
print(time_function(solve))
