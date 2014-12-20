import sys, time

def check(n,base):
	for i in base:
		if not check_pair(i,n):
			return False
	return True

def check_pair(a,b):
	return prime(concatints(a,b)) and prime(concatints(a,b))

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

def get_next_prime(n):
	i = n+1
	while True:
		if prime(i):
			return i
		i += 1

p = []

i = get_next_prime(0)
start = time.time()
while i < 20000:
	p.append(i)
	i = get_next_prime(i)
print "Primes Generated ",time.time()-start,"ms" 

L = len(p)
start = time.time()
a = 1
log = []
while a < L: 
	print "a = ", a
	b = a + 1
	while b < L:
		c = b + 1
		while c < L:
			d = c + 1
			while d < L:
				e = d + 1
				while e < L:
					#print "a:",a,"b:",b,"c:",c,"d:",d,"e:",e
					if check(p[e],[p[a],p[b],p[c],p[d]]):
						log.append([p[a],p[b],p[c],p[d],p[e]])
					e += 1
				d += 1
			c += 1
		b += 1
	a += 1
print "Solved",time.time()-start,"ms" 

for i in log:
	print i, sum(i)

print len(pairs)
