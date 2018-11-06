from timer import time_function
from math import factorial
def f(x):
    return 1 if x < 2 else x*f(x-1)

def f1(x):
    return factorial(x) 

N = 100000
s = 0
x = 10
for n in range(N):
    s += time_function(f,x)[1]
print('x*x',s/N)

s = 0
for n in range(N):
    s += time_function(f1,x)[1]
print('x**2',s/N)
