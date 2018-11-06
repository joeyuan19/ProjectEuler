from timer import time_function

def pad(n,pad_length):
    s = len(n)
    return '0'*max(0,pad_length-s)+n

def subsets(s):
    n = 0
    L = len(s) 
    for n in range(1,2**(L-1)):
        a,b = [],[]
        _n = pad(str(bin(n)).lstrip('0b'),L)
        for i,_s in enumerate(_n):
            if _s == '0':
                a.append(s[i])
            else:
                b.append(s[i])
        yield a,b

def test_subsets(a,b):
    return not sum(a) == sum(b) 

def is_special(s):
    L = len(s)
    if L != len(set(s)):
        #print('bail',0)
        return False
    ss = sorted(s)
    for i in range(L-1,L//2,-1):
        for j in range(2,i+1):
            if j > L-i and not sum(ss[:j]) > sum(ss[i:]):
                #print('bail',1)
                return False
    for a,b in subsets(s):
        if not test_subsets(a,b):
            #print('bail',2)
            return False
        for c,d in subsets(b):
            if not test_subsets(a,c):
                #print('bail',3)
                return False
            elif not test_subsets(a,d):
                #print('bail',4)
                return False
        for c,d in subsets(a):
            if not test_subsets(b,c):
                #print('bail',5)
                return False
            elif not test_subsets(b,d):
                #print('bail',6)
                return False
    return True

def generate_sums(s,depth=0):
    L = len(s)
    if L > 1:
        while True:
            for _s in generate_sums(s[1:],depth=depth+1):
                yield [s[0]] + _s
            done = True
            for i in range(L):
                for j in range(i+1,L):
                    if s[i]-s[j] > 1:
                        s[i] = s[i]-1
                        s[j] = s[j]+1
                        done = False
                        break
                if not done:
                    break
            if done:
                break
    else:
        yield s

def generate_sets(n):
    s = [1]*n
    S = n
    while True:
        u = True
        s0 = s[0]
        for i in range(1,n):
            if s[i] < s0: 
                s[i] = s[i] + 1
                for j in range(i+1,n):
                    s[j] = 1 
                u = False
                break
        if u:
            s = [s[0] + 1] + [1]*(n-1)
        yield s


def nearby_search_solve():
    s = [11, 18, 19, 20, 22, 25]
    smid = s[len(s)//2+1]
    s0 = [smid] + [smid+i for i in s]
    N = 5
    itr = [N]*len(s0)
    m = sum(s0)
    while sum(itr) != 0:
        s = tuple(i-j for i,j in zip(s0,itr))
        if is_special(s):
            if sum(s) < m:
                m = sum(s)
                ms = s
        # increment
        last = itr[0]
        itr[0] = (itr[0]-1)%(N+1)
        for i in range(1,7):
            if last == 0:
                last = itr[i]
                itr[i] = (itr[i]-1)%(N+1)
            else:
                break
    return ''.join(str(i) for i in sorted(ms))

print(time_function(nearby_search_solve))

#print(is_special([6, 9, 11, 12, 13]))
import sys
sys.exit()

sp = [1]
N = 1
last = N
for n in range(2,7):
    l = len(sp)
    sp_mid = sorted(sp)[max(0,l//2)]
    n0 = sum(range(1,n+1))
    s0 = n*sp_mid+sum(sp)
    print('n =',n)
    print('sp =',sp,'sp_mid =',sp_mid,'sum(sp) =',sum(sp),'n*sp_mid =',n*sp_mid)
    print('n0 =',n0,'s0 =',s0,end=' ')
    N = max(n0,s0)
    print('N =',N)
    while True:
        print(N,s0)
        found = False
        for s in generate_sums([1+N-n]+[1]*(n-1)):
            if is_special(s):
                sp = s
        if N <= s0:
            print('n =',n,'S(A) =',sum(sp),'A =',sp)
            break
        N += 1

