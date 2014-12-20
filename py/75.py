import sys

def inorder(list):
	for i in range(len(list)-1):
		if list[i] > list[i+1]:
			return False
	return True

def catalogue(list):
	cat = []
	exists = False
	for i in list:
		for index in range(len(cat)):
			if i == cat[index][0]:
				cat[index][1] += 1
				exists = True
				break
		if not exists:
			cat.append([i,1])
	for i in cat:
		print i[0],":",i[1]

def sort(list):
	if inorder(list): return list
	return mergesort(list)

def insertsort(list):
	L = len(list)
	while not inorder(list):
		for i in range(L):
			print i
			min = list[i]
			index = i
			for j in range(i+1,L):
				if min > list[j]:
					min = list[j]
					index = j
			temp = list[index]
			list[index] = list[i]
			list[i] = temp
	return list

def mergesort(list):
	L = len(list)
	print L
	if L > 2:
		mid = len(list)/2
		l1 = mergesort(list[:mid])
		l2 = mergesort(list[mid:])
		i1 = 0
		i2 = 0
		i = 0
		while i < L:
			if i >= L:
				break
			elif i1 >= len(l1) and i2 >= len(l2) :
				break
			elif i1 >= len(l1):
				list[i] = l2[i2]
				i2 += 1
			elif i2 >= len(l2):
				list[i] = l1[i1]
				i1 += 1	
			elif l1[i1] > l2[i2]:
				list[i] = l2[i2]
				i2 += 1
			else:
				list[i] = l1[i1]
				i1 += 1
			i += 1
	elif L == 2:
		if list[0] > list[1]:
			temp = list[0]
			list[0] = list[1]
			list[1] = temp
	return list

def gcd(x,y):
	if x > y:
		n = x
	else:
		n = y
	i = n
	while i > 0:
		if x%i == 0 and y%i == 0:
			return i
		i += -1
	return 1

def getSingles(list):
	sort(list)
	print inorder(list)
	L = len(list)
	i = 0
	n = 0
	while i < L:
		print i, L
		if i < L - 1:
			j = i + 1
			if list[i] != list[j]:
				n += 1
			else:
				while list[i] == list[j]:
					j += 1
					if j >= L:
						return n
				i = j - 1
		elif i == L - 1:
			n += 1
		i += 1
	return n

N = 1500000
trips = []
n = 0

# m > n
# m - n odd
# gcd(m,n) = 1

limit = N**.5 + 1 

while n < limit:
	print n, limit
	n += 1
	m = n
	while m < limit:
		m += 1
		if (m-n)%2 == 1 and gcd(m,n) == 1:
			k = 1
			trip = -1
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			while trip < N:
				trip = k*(a+b+c)
				trips.append(trip)
				k += 1

print getSingles(sorted(trips))

