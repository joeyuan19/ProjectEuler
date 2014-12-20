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
    s = [1,1,0]+[0,1]*N
    for i in range(3,int(N**.5)+1,2):
        itr = i*2
        while itr < N:
            s[itr] += 1
            itr += i
    return [i for i in range(N) if s[i] == 0]


