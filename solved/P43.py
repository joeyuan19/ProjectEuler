def listToNum(list):
	s = ""
	for i in list:
		s += str(i)
	return int(s)

def sorted(list):
	for i in range(len(list)-1):
		if list[i] > list[i+1]:
			return False
	return True

def sort(list0,init=0,final=-1):
	if init < 0:
		init = len(list0) + init
	if final < 0:
		final = len(list0) + 1 + final
	list = [i for i in list0[init:final]]
	while not sorted(list):
		for i in range(len(list)-1):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
	j = 0
	for i in range(init,final):
		list0[i] = list[j]
		j += 1
	return list0

def find_closest_above(n,list):
	d = -1
	index = -1
	for i in range(len(list)):
		if list[i] > n:
			if d < 0:
				d = list[i] - n
				index = i
			elif list[i] - n < d:
				d = list[i] - n
				index = i
	return index - len(list), list[index]
		
	

def permute(list):
	for i in range(1,len(list)):
		if list[-i] > list[-(i+1)]:
			index, temp = find_closest_above(list[-(i+1)],list[-i:])
			list[index] = list[-(i+1)]
			list[-(i+1)] = temp
			sort(list,-i)
			return list
	return sort(list)

def fact(n):
	if n < 0:
		return 0
	if n > 1:
		return n*fact(n-1)
	else:
		return 1

def check(number):
	p = [2,3,5,7,11,13,17]
	for i in range(len(p)):
		if listToNum(number[i+1:i+4])%p[i] != 0:
			return False
	return True

number = [1,0,2,3,4,5,6,7,8,9]


i = 0
N = 9*fact(9)

print N
sum = 0

while i < N:
	print i
	if check(number):
		sum += listToNum(number)
	i += 1
	permute(number)

print sum
	

