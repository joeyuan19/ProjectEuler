class Done(Exception):
    pass

def pent(n):
    return n*(3*n-1)/2

p = [1]
n = 1
while True:
    print n
    s = 0
    i = 1
    while True:
        try:
            for k in (i,-i):
                d = pent(k)
                if (k-1)%2 == 1:
                    sign = -1
                else:
                    sign = 1
                if n-d < 0:
                    raise Done()
                else:
                    s = (s + sign*p[n-d])%(10**6)
        except Done:
            break
        i += 1
    if s%10**6 == 0:
        print "Answer:",n
        break
    p.append(s)
    n += 1


