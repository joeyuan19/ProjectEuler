from math import log10 as log

def point_generator(n):
	temp = set()
	for i in range(2*n + 1):
		temp.add((2**i % n, 3**i % n))
	temp = [i for i in temp]
	temp.sort()
	return [[j for j in i] for i in temp]

def graph(list,n):
	s = ""
	empty = len(list) <= 0
	print empty
	X = [x[0] for x in list]
	Y = [y[1] for y in list]
	print X,Y
	x_offset = int(log(n))
	y_offset = int(log(n))
	for i in range(0,n+1):
		s += str(n-i)
		if n-i > 0:
			dif = int(log(n-i))
		elif n-i == 0:
			dif = 0
		else:
			dif = int(log(-i+n)) + 1
		for k in range(int(y_offset-dif)):
			s += " "
		for j in range(0,n+1):
			if j > 0:
				dif = int(log(j))
			elif j == 0:
				dif = 0
			else:
				dif = int(log(-j))
			s += " "
			for k in range(x_offset):
				s += " "
			if not empty:
				if n-i in Y and j in X and Y.index(n-i) == X.index(j):
					Y.pop(Y.index(n-i))
					X.pop(X.index(j))
					s += "o"
				else:
					s += "."
			else:
				s += "."
		s += '\n'
	s += "  " 
	for i in range(n+1):
		if i > 0: dif = int(log(i))
		elif i == 0: dif = 0
		else: dif = int(log(-i))
		s += " "
		for j in range(int(x_offset - dif)):
			s += " "
		s += str(i)
	return s

n = 22

points = point_generator(n)
print points
print graph(points,n)


