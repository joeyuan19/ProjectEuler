import sys, time


def concatints(a,b):
  return int(str(a) + str(b))

def prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n%2 == 0:
		return False
	else:
		i = 3
		while i < n**.5:
 			if n%i == 0:
				return False
			i += 2
		return True

def primepair(x,y):
	if not prime(concatints(x,y)):
		return False
	elif not prime(concatints(y,x)):
		return False
	return True

def check(list, sieve):
	L = len(list)
	Lp = len(sieve)
	for i in range(L-1):
		for j in range(L):
			if concatints(list[i],list[j]) < sieve[-1] and concatints(list[j],list[i]) < sieve[-1]:
				if concatints(list[i],list[j]) not in sieve or concatints(list[j],list[i]) not in sieve:
					return False
			elif not primepair(list[i],list[j]):
				return False
	return True

def sum(a):
	s = 0
	for i in a:
		s += i
	return s

def dif(a,b):
	if len(a) > len(b):
		return [x for x in b if x not in a]
	else:
		return [x for x in a if x not in b]

def inter(a,b):
	if len(a) > len(b):
		return [x for x in b if x in a]
	else:
		return [x for x in a if x in b]

def Sieve(N):
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

N = 1000
n_a = 4

p = Sieve(N)
L = len(p)

for i in range(L):
	for j in range(i+1,L):
		if i != j:
			for k in range(j+1,L):
				if k != j and k != i:
					for l in range(k+1,L):
						print i,j,k,l,L
						if l != k and l != j and l != i:
							a = [p[i],p[j],p[k],p[l]]
							if check(a,p):
								print a
							#for n in range(l+1,L):
							#	if n != l and n != k and n != j and n != i:

sys.exit()

pairs = {}
print L,"primes created"

start = time.time()

for i in range(L):
	temp = []
	for j in range(L):
		if i != j:
			if concatints(p[i],p[j]) < p[-1] and concatints(p[j],p[i]) < p[-1]:
				if concatints(p[i],p[j]) in p and concatints(p[j],p[i]) in p:
					temp.append(p[j])
			else:
				if primepair(p[i],p[j]):
					temp.append(p[j])
	pairs[p[i]] = temp
	del(temp)
	temp = []

Lpairs = len(pairs)
print Lpairs,"pairs found"
chain = []
rel_groups = []

for prime in p:
	if len(pairs[prime]) > n_a:
		rel_groups.append(pairs[prime])

print len(rel_groups),"relvent groups found"

print time.time() - start


