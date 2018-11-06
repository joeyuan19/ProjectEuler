
def prime(n):
	if n < 2:
            return False
	if n == 2:
            return True
	elif n%2 == 0:
            return False
	else:
            i = 3
            while i < n**.5 + 1:
                if n%i == 0:
                    return False
                i += 2
            return True


def solve():
    ratio = .1
    d = 0
    n = 1
    p = 0.0

    while 1:
        d += 2
        for i in range(3):
            n += d
            if prime(n): p += 1.0
        n += d
        print(p/(2*d + 1))
        if p/(2.*(d+1) - 1) < ratio:
            break	
    print(d + 1, p)
    print('\n', str(int(100*p/(2*(d+1) - 1))) + "%")

from timer import time_function
print(time_function(solve))



