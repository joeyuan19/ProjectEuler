def subrects(W,H):
    s = 0
    for w in range(1,W+1):
        for h in range(1,H+1):
            s += (W-w+1)*(H-h+1)
    return s

def solve():
    L = 500

    MM = 2000000
    d = MM
    ld = MM
    N = MM

    for W in range(1,L):
        ld = MM
        for H in range(W,L):
            n = subrects(W,H)
            diff = abs(MM-n)
            if diff < d:
                d = diff 
                N = n
                _w,_h = W,H
            elif diff > ld:
                break
            ld = diff

    #print "Limit:",L
    #print "(w,h) = ("+str(_w)+","+str(_h)+")"
    #print "Area:",_w*_h
    #print "Subrects:",N
    #print "Diff:",d
    return _w*_h

from timer import time_function
print(time_function(solve))
