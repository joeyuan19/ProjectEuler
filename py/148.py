import math

class Factorial(object):
    def __init__(self):
        self.table = [1]

    def factorial(self,N):
        return math.factorial(N)

    def _factorial(self,N):
        if len(self.table)-1 < N:
            for i in range(len(self.table),N+1):
                print i
                self.table.append(self.table[i-1]*i)
        return self.table[N]
    
def binomial(n,k,f):
    return f.factorial(n)/(f.factorial(k)*f.factorial(n-k))

def pascal(row,f):
    last = 1
    yield 1
    for i in xrange(1,row+1):
        last = last*(row+1-i)/i
        yield last
    

MAX = 10**4
c = 0
f = Factorial()

for N in xrange(MAX):
    print N
    for i in pascal(N,f):
        if i%7 != 0:
            c += 1
print "done",c

