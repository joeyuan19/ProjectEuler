i = 1
e = [2]
while len(e) < 100:
    e.append(1)
    e.append(i*2)
    e.append(1)
    i += 1

def converge(e,N):
    n = 1
    d = e[N-1]
    for i in xrange(N-2,-1,-1):
        n = n + d*e[i]
        d,n = n,d
    return d,n


print sum(int(i) for i in str(converge(e,100)[0]))
