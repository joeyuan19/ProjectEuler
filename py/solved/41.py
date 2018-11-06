def pancheck(x):
	s = str(x)
	l = len(s)
	for i in range(1,l+1):
		if str(i) not in s:
			return False
	return True

def prime(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if x%2 == 0:
		return False
	for i in range(3,x,2):
		if x%i == 0:
			return False
	return True
def solve():
    N = 1000000000
    m = 0
    i = 1
    while i < N:
            if pancheck(i):
                    if prime(i):
                            m = i
            i += 1
    return m

from timer import time_function
print(time_function(solve))
