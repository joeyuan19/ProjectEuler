def solve():
    N = 10**6
    md = 1
    mn = 0


    for d in range(2,N+1):
        n = int((3./7)*d)
        if float(n)/d > float(mn)/md and float(n)/d < 3./7:
            mn = n
            md = d
    #print("Best match:",mn,"/",md)
    return mn

from timer import time_function
print(time_function(solve))
