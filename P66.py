import math

max = 0
Dmax = 0

N = 200

for D in range(1,N+1):
	if math.sqrt(D) != int(math.sqrt(D)):
		print D
		x = 1
		y = 1
		while x != float(1 + D*y*y)/x:
			while x > float(1 + D*y*y)/x:
				y += 1
			if x == float(1 + D*y*y)/x:
				break
			else:
				y = 1
				x += 1
		if x > max:
			max = x
			Dmax = D
print max, Dmax
