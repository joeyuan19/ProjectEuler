from totient import totients

def solve(): return sum(i for i in totients(10**6)[2:])

from timer import time_function
print(time_function(solve))
