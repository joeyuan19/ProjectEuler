def first_sol(D):
    x = 1
    while True:
        y = 1
        while x*x - D*y*y > 1:
            y += 1
        if x*x - D*y*y == 1:
            return x,y
        x += 1
D = 1000
m = -1
for N in xrange(D+1):
    print N 
    if int(N**.5) != N**.5:
        x,y = first_sol(N)
        if x > m:
            m = x
            d = N
print d,m



