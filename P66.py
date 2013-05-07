N = 1000

dio = [d for d in range(2,N+1) if d**.5 != int(d**.5)]

Dmax = 1001
xmax = 0

for D in dio:
	x = 0
	y = 1
#	print D
	while x**2 - D*(y**2) != 1:
		y = 1
		x += 1
		while x**2 > D*(y**2) + 1:
			y += 1
			print D, y
	print str(x) + "^2 - " + str(D) + "x" + str(y) + "^2 = 1"
#print x
	if x > xmax:
		Dmax = D
		xmax = x
print Dmax
