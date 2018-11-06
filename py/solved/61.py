'''
Problem 61

Solution description:
    Solution space is 6! type orderings with roughly 40*50*60*70*80*90 possible values.  Rather large, but the following steps can it down plenty.
    - Resolve the space of 4-digit numbers of each type: triangular, square, ...
    - Map the space between each (number,type) where they share the first and last two digits
    - Search the space of all the unique type orderings
    - Explore each ordering using the list of pre determined leading numbers to shrink the search space 
'''



import itertools

def tri(n):
    return n*(n+1)/2

def sq(n):
    return n*n

def pent(n):
    return n*(3*n-1)/2

def hexa(n):
    return n*(2*n-1)

def hep(n):
    return n*(5*n - 3)/2

def octa(n):
    return n*(3*n - 2)

def permutes(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s[i:]+s[:i])

def solve():
    data = {
        tri:[],
        sq:[],
        pent:[],
        hexa:[],
        hep:[],
        octa:[]
    }
    leads = {
        tri:{},
        sq:{},
        pent:{},
        hexa:{},
        hep:{},
        octa:{}
    }
    names = {
        tri:'tri',
        sq:'sq',
        pent:'pent',
        hexa:'hex',
        hep:'hep',
        octa:'oct'
    }

    for f in data:
        n = -1
        i = 1
        s = 0
        while len(str(n)) < 5:
            if len(str(n)) == 4:
                data[f].append(str(n))
            n = f(i)
            i += 1

    for g in data:
        for itr in data[g]:
            a = []
            for f in data:
                if f == g:
                    continue
                for i in data[f]:
                    if i.startswith(itr[-2:]):
                        a.append((i,f))
            leads[(itr,g)] = a
    
    L = 6
    for outline in itertools.permutations([i for i in data],L):
        for n in data[outline[0]]:
            a = (n,outline[0])
            for b in leads[a]:
                if b[1] == outline[1]:
                    for c in leads[b]:
                        if c[1] == outline[2]:
                            for d in leads[c]:
                                if d[1] == outline[3]:
                                    for e in leads[d]:
                                        if e[1] == outline[4]:
                                            for f in leads[e]:
                                                if f[1] == outline[5] and a in leads[f]:
                                                    print(a,b,c,d,e,f)
                                                    print(sum(int(j[0]) for j in (a,b,c,d,e,f)))

from timer import time_function
print(time_function(solve))
