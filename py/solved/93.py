from timer import time_function
import itertools

DIGITS = tuple(str(i) for i in range(1,10))
SYMBOLS = ["*","/","-","+"]
PEMDAS = "*/-+"

def operate(op,a,b):
    a,b = tuple(map(int,(a,b)))
    return str({'*':(lambda a,b: a*b),
            '/':(lambda a,b: a/b),
            '+':(lambda a,b: a+b),
            '-':(lambda a,b: a-b)}[op](a,b))

# e = expression
# s = stack
def calculator(e):
    s = []
    L = len(e)
    i = 0
    while i < L:
        if e[i] == "(":
            p = 1
            j = i+1
            while j < L:
                if e[j] == ")":
                    p -= 1
                elif e[j] == "(":
                    p += 1
                if p == 0:
                    s.append(calculator(e[i+1:j]))
                    i = j + 1
                    break
                j += 1
        else:
            s.append(e[i])
            i += 1
    for o in PEMDAS:
        try:
            idx = s.index(o)
        except ValueError:
            continue
        i = 0
        while True:
            try:
                s = s[:idx-1]+[operate(s[idx],s[idx-1],s[idx+1])]+s[idx+2:]
                idx = s.index(o)
            except ValueError:
                break 
            i += 1
    r = s.pop()
    return str(r)

OP = ['+','+','+',
      '-','-','-',
      '*','*','*',
      '/','/','/']

"""
a+b+c+d            *
(a)+b+c+d          
(a+b)+c+d          *
(a+b+c)+d          *
    ((a)+b+c)+d    *
    ((a+b)+c)+d    *
    (a+(b+c))+d    *
(a+b+c+d)          
a+(b)+c+d          *
"""

def gen_exp(n):
    for po in itertools.combinations(OP, 3):
        for pn in itertools.permutations(n):
            e = ''
            for i,j in zip(po,pn):
                e += j + i
            yield e + pn[-1]
        




# Treat paranthesis as arbitraries breaks


def combine(a,b):
    yield a+b
    yield a*b
    try:
        yield a/b
    except ZeroDivisionError:
        pass
    try:
        yield b/a
    except ZeroDivisionError:
        pass
    yield a-b
    yield b-a

def combos(a,b,c,d):
    for ab in combine(a,b):
        for cd in combine(c,d):
            for r in combine(ab,cd):
                yield r
        for abc in combine(ab,c):
            for r in combine(abc,d):
                yield r
    for bc in combine(b,c):
        for abc in combine(a,bc):
            for r in combine(abc,d):
                yield r
        for bcd in combine(bc,d):
            for r in combine(a,bcd):
                yield r
    for cd in combine(c,d):
        for bcd in combine(b,cd):
            for r in combine(a,bcd):
                yield r

def exps(n):
    for pn in itertools.permutations(n):
        for el in combos(*pn):
            yield el

def solve():
    MAX = 9*8*7*6
    nmax = 0
    for i in range(1,10):
        for j in range(i+1,10):
            for k in range(j+1,10):
                for l in range(k+1,10):
                    a = set(tuple(i for i in exps([i,j,k,l])))
                    for n in range(1,MAX+1):
                        if n not in a:
                            if n > nmax:
                                nmax = n
                                smax = [i,j,k,l]
                            break
    return ''.join(str(i) for i in smax)

print(time_function(solve))

