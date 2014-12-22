def area(a):
    return _area(a,a+1)

def _area(a,b):
    try:
        return .5*b*(a*a - (b*b/4.))**.5
    except ValueError:
        return -.1

def perim(a):
    return _perim(a,a+1)

def _perim(a,b):
    return 2*a+b

def is_int(n):
    return n == int(n)

LIMIT = 10**9

a = 1
s = 0
while perim(a) < LIMIT:
    if is_int(area(a)):
        s += perim(a)
    a += 2

print s
