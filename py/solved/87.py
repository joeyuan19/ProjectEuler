import time
import sys

def prime(x):
        if x < 2:
                return False
        if x == 2:
                return True
        if x%2 == 0:
                return False
        for i in range(3,x,2):
                if x%i == 0:
                        return False
        return True

def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(N**.5)+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]

def solve():
    N = 50000000

    p = Sieve(int(N**.5 + 24)+1)
    sq = [i**2 for i in p if i**2 + 24 < N]
    cu = [i**3 for i in p if i**3 + 20 < N]
    fo = [i**4 for i in p if i**4 + 12 < N]

    nums = set([a+b+c for a in sq for b in cu for c in fo if a+b+c < N])
    return len(nums)

from timer import time_function
print(time_function(solve))

"""
    total = float(len(sq))*len(cu)*len(fo)
    print total

    start = time.time()
    for a in sq:
            if a + cu[0] + fo[0] > N:
                    i += len(sq)
                    break
            for b in cu:
                    if a + b + fo[0] > N:
                            i += len(cu)
                            break
                    for c in fo:
                            if a + b + c > N:
                                    i += len(fo)
                                    break
                            n = a + b + c
                            if n < N: 
                                    if n not in nums:
                                            nums.append(n)
            print total - i
    print len(nums)
    sys.exit()

    print L
    print p
    nums = []


    start = time.time()
    for c in range(L):
            print c
            if p[c]**2 > N:
                    break
            for b in range(L):
                    print " ", b
                    if p[c]**2 + p[b]**3 > N:
                            break
                    for a in range(L):
                            print "  ", a
                            n = p[c]**2 + p[b]**3 + p[a]**4
                            if n > N:
                                    break
                            if n < N and n not in nums:
                                    nums.append(n)
                                    total += 1
#				print total
    print nums
    print len(nums)
    print time.time() - start 

    while i < N:
            a = 1
            b = 1
            c = 1
            found = False
            while c**4 <= i:
                    while c**4 + b**3 <= i:
                            while c**4 + b**3 + a**2 <= i:
                                    if a**2 + b**3 + c**4 == i and prime(a) and prime(b) and prime(c):
                                            total += 1
                                            print total
                                            found = True
                                            break
                                    a += 1
                            if found: break
                            b += 1
                            a = 1
                    if found: break
                    c += 1
                    a = 1
                    b = 1
            i += 1

    """
