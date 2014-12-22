def prime(n):
    if n%2 == 0:
        return False
    i = 3
    while i*i < n:
        if n%i == 0:
            return False
        i += 2
    return True

def sieve(N):
    s = [0,0,1]+[1,0]*(N/2)
    i = 3
    while i*i < N:
        if s[i]:
            for itr in xrange(i*2,N,i):
                s[itr] = 0
        i += 2
    return [i for i in range(N) if s[i]==1]


