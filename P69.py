def tot(n):
	rel_prime = n - 1
	print n, ": 1",
	for i in range(2,n):
		if n%i == 0:
			rel_prime = rel_prime - (n/i - 1)
		else:
			print i,
	print ":",rel_prime
	return rel_prime

N = 10

for i in range(2,N+1):
	tot(i)

