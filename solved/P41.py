def pancheck(x):
	s = str(x)
	l = len(s)
	for i in range(1,l+1):
		if str(i) not in s:
			return False
	return True

def prime(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if x%2 == 0:
		return False
	for i in range(3,x,2):
		if x%i == 0:
			return False
	return True

N = 1000000000
max = 0
i = 1
while i < N:
	if pancheck(i):
		if prime(i):
			max = i
			print max
	i += 1
print max


