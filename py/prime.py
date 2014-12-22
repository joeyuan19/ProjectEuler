def iprime(n):
    if n%2 == 0:
        return False
    i = 3
    while i*i < n:
        if n%i == 0:
            return False
        i += 2
    return True

def sieve(N):
    s = [False,False,True]+[True,False]*N
    for i in xrange(3,int(N**.5)+1,2):
        if s[i]:
            itr = i*2
            while itr < N:
                s[itr] = False 
                itr += i
    return [i for i in range(N) if s[i]]


