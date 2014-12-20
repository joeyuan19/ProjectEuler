import sys

def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(N**.5)+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(n**.5) + 1,2):
        if n%i == 0:
            return False
    return True

def intToList(x):
	return [int(i) for i in str(x)]

def listToInt(list):
	s = ""
	for i in list:
		s += str(i)
	return int(s)

def cycle(x,list):
	n = 0
	temp = [i for i in list]
	if list[0] == 0:
		for j in range(10):
			for i in range(len(list)):
				if list[i] == x:
					temp[i] = j
			if prime(listToInt(temp)):
				n += 1
	else:
		for j in range(1,10):
			for i in range(len(list)):
				if list[i] == x:
					temp[i] = j
			if prime(listToInt(temp)):
				n += 1
		
	return n

def getNumPrimes(x):
	list = intToList(x)
	max_numPrimes = 0
	for i in range(10):
		if i in list:
			n = cycle(i,list)
			if n > max_numPrimes:
				max_numPrimes = n
	return max_numPrimes

n = 0
i = 0
while n != 8:
	i += 1
	print i
	if prime(i):
		n = getNumPrimes(i)
print n, i

