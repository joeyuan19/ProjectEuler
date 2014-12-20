from random import randint as R

p = 0
c = 0

w = 0
w_ave = 0
N = 1000000
M = 5

for j in range(M):
	for k in range(N):
		for i in range(9):
			p += R(1,4)
		for i in range(6):
			c += R(1,6)
		if p > c:
			w += 1
		p = 0
		c = 0
	print float(w)/N
	w_ave += w
	w = 0

print float(w_ave)/M/N
