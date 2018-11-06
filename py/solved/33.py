n = 10
d = 10
"""
for d in range(10,100):
	ds = str(d)
	for n in range(10,d):
		ns = str(n)
		for k in range(len(ns)):
			for l in range(len(ds)):
				if ns[k] == ds[l]:
					if int(ds[(l+1)%2]) != 0 and float(ns)/float(ds) != 1:
						if (float(ns)/float(ds)) == float(ns[(k+1)%2])/float(ds[(l+1)%2]):
							print float(ns)/float(ds), float(ns[(k+1)%2])/float(ds[(l+1)%2]), ns, ds
"""
"""
16 64
26 65
19 95
49 98
"""

def solve():
    n = [16,26,19,49]
    d = [64,65,95,98]

    N = 1
    D = 1

    for i in range(len(n)):
            N = N*n[i]
            D = D*d[i]

    #print N, D

    for i in range(N+1,1,-1):
            if D%i == 0 and N%i == 0:
                    D = D/i
                    N = N/i
                    i = N
    return N, D

from timer import time_function
print(time_function(solve))
