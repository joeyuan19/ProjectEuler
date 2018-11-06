from timer import time_function

def pad(n,pad_length=2):
    s = str(n)
    return "0"*max(0,(pad_length-len(s)))+s

def generate_squares():
    for i in range(1,10):
        yield i*i

def inc(d,m=9):
    i = 1
    while d[-i] == m-(i-1):
        i += 1
    d[-i] += 1
    j = -i+1
    k = 1
    while j < 0:
        d[j] = d[-i]+k
        k += 1
        j += 1
    return d

def generate_dice():
    d1 = [0,1,2,3,4,5]
    d2 = [0,1,2,3,4,5]
    while d1 != [3,4,5,6,7,8]:
        while d2 != [3,4,5,6,7,8]:
            yield d1,d2
            inc(d2)
        yield d1,d2
        inc(d1)
        d2 = [i for i in d1]
    while d2 != [3,4,5,6,7,8]:
        yield d1,d2
        inc(d2)
    yield d1,d2

def solve():
    matches = 0
    for d1,d2 in generate_dice():
        match = True
        for sq in generate_squares():
            s = pad(sq)
            a,b = tuple(map(int,tuple(s)))
            a = (a,) if a not in (6,9) else (6,9)
            b = (b,) if b not in (6,9) else (6,9)
            if any(_a in d1 for _a in a) and any(_b in d2 for _b in b):
                continue
            elif any(_a in d2 for _a in a) and any(_b in d1 for _b in b):
                continue
            else:
                match = False
                break
        matches += match
    return matches

print(time_function(solve))

