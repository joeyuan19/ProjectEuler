from totient import totients
import time

N = 10**7
L = N+1
t = totients(N)
print min((float(i)/t[i],i) for i in xrange(2,L) if sorted(str(i)) == sorted(str(t[i])))
