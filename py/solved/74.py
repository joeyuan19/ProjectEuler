def fact(x):
	if  x > 1:
		return x*fact(x-1)
	else:
		return 1

def f(x):
	x = str(x)
	s = 0
	for i in x:
		s += fact(int(i))
	return int(s)

def solve():
    N = 1000000
    total = 0
    for i in range(N):
            print(i)
            temp = []
            x = i
            while x not in temp:
                    temp.append(x)
                    x = f(x)
            if len(temp) == 60:
                    total += 1
    return total

from timer import time_function
print(time_function(solve))
