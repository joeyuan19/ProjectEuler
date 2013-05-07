import sys
import random
import time

def inorder(list):
	i = 0
	L = len(list)
	while i < L - 1:
		if list[i] > list[i+1]:
			return False
		i += 1
	return True

def insertSort(list):
	L = len(list)
	if inorder(list):
		return list
	i = 0
	while i < L:
		j = i + 1
		min = list[i]
		index = i
		while j < L:
			if list[j] < min:
				min = list[j]
				index = j
			j += 1
		temp = list[i]
		list[i] = list[index]
		list[index] = temp
		i += 1
	return list

def mergeSort(list):
	if inorder(list): return list
	L = len(list)
	if L > 1:
		if L == 2:
			if list[0] > list[1]:
				temp = list[1]
				list[1] = list[0]
				list[0] = list[1]
			return list
		mid = L/2
		l1 = mergeSort(list[:mid])
		l2 = mergeSort(list[mid:])
		L1 = len(l1)
		L2 = len(l2)
		i1 = 0
		i2 = 0
		i = 0
		while i < L:
			if i >= L:
				break
			if i1 >= L1 and i2 >= L2:
				break
			elif i1 >= L1:
				list[i] = l2[i2]
				i2 += 1
			elif i2 >= L2:
				list[i] = l1[i1]
				i1 += 1
			elif l1[i1] > l2[i2]:
				list[i] = l2[i2]
				i2 += 1
			else:
				list[i] = l1[i1]
				i1 += 1
			i += 1
	return list	

def bubbleSort(list):
	L = len(list)
	swap = True
	while swap:
		swap = False
		i = 0
		while i < L - 1:
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
				swap = True
			i += 1
	return list

def newsort(list):
	if inorder(list):
		return list
	
	return list

def testsort(sort,v=True):
	list = [9,7,4,8,3,7,4,3,6,2,6,8,9,5,2,5,2,1,7,1,6,3,7,9,4,2,8,3]
	start = time.time()
	sort(list)
	if v: print time.time() - start
	return inorder(list)

def comparesorts(sort1,sort2):
	test = [4,3,1,6,5,2,8,9]
	if testsort(sort1,v=False) and testsort(sort2,v=False):
		t1 = 0
		t2 = 0
		for j in range(10):
			list = [random.randint(0,10) for i in range(100)]
			start = time.time()
			sort1([i for i in list])
			t1 += time.time() - start
			start = time.time()
			sort2([i for i in list])
			t2 += (time.time() - start)
		if t2/5 > t1/5:
			print "sort 1 performed better on average"
		else:
			print "sort 2 performed better on average"

print "bubble vs merge"
comparesorts(bubbleSort,mergeSort)
print "insert vs merge"
comparesorts(insertSort,mergeSort)
print "insert vs bubble"
comparesorts(insertSort,bubbleSort)

