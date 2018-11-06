from timer import time_function

def solve():
    N = 1000000
    N = int(N) + 1
    s = [0,0] + [1]*N

    for i in range(2,N):
        for j in range(2*i,N,i):
            s[j] += i

    b = set(i for i in s if i < N)
    ml = 0
    for n in b:
        c = [n]
        _n = s[n]
        while 2 < _n < N:
            if _n in c:
                c = c[c.index(_n):]
                l = len(c)
                if ml < l:
                    ml = l
                    mc = c
                break
            c.append(_n)
            _n = s[_n]
    return min(mc)

print(time_function(solve))
