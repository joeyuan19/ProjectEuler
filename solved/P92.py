total = 0
N = 10**7
a = [44, 85]

for i in range(1,N):
	temp = i
	if i%100 == 0: print i
	while temp != 1 and temp != 89:
		#print temp, "->",
		sum = 0
		nstr = str(temp)
		for j in range(len(nstr)):
			sum += int(nstr[j])**2
		temp = sum
	#print temp
	if temp == 89:
		total += 1

print total
