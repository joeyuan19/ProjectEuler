M = 100

while True:
    count = 0
    for a in xrange(1,M+1):
        for b in xrange(a,M+1):
            for c in xrange(b,M+1):
                shortest = min(((a+b)**2 + c**2)**.5,((b+c)**2 + a**2)**.5,((c+a)**2 + b**2)**.5)
                if shortest == int(shortest):
                    count += 1
    if count > 10**6:
        print M
        break
    M += 1

