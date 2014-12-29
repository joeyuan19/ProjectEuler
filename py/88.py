def prod(li):
    p = 1
    for i in li:
        p = p*i
    return p

def inc(li):
    l = len(li)
    for j in xrange(1,l):
        if li[j] < li[0]:
            return li[:j]+inc(li[j:])
    return [li[0]+1]+[1]*(l-1) 


N = 12000
sols = []
for k in xrange(2,N+1):
    print float(k)/N
    arr = [1]*k
    while True: 
        if sum(arr) == prod(arr):
            sols.append(arr)
            break
        arr = inc(arr)

sol = []
for s in sols:
    if sum(s) not in sol:
        sol.append(sum(s))
print sum(sol)

