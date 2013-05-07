def divsum(n):
	i = 1
	sum = 0
	if n <= 1 :
		return 1
	while i < n**.5:
		if n%i == 0:
			sum += i + n/i
		i += 1
	return sum - n

def getMin(list):
	L = len(list)
	if L == 0:
		return Null
	min = list[0]
	i = 0
	while i < L:
		if min > list[i]:
			min = list[i]
		i += 1
	return min

min = -1
chain = []
N = 1000000
ref = {}

for i in range(N+1):
	print i
	ref[i] = divsum(i)

j = 10
length = 0
Lmin = 0
chains = {}
prev_searched = False


while j < N:
	i = j
	print j
	while i not in chain:
		if i in chains:
			prev_searched = True
			break
		chain.append(i)
		#print i,
		i = ref[i]
		if i > N:
			break
	if not prev_searched:
		if i < N and length < len(chain):
			max_chain = [i for i in chain]
		if i < N:
			chains[j] = len(chain)
		
	else:
		if i < N and length < len(chain) + chains[i]:
			max_chain = [k for k in chain]
		if i < N:
			chains[j] = len(chain) + chains[i]
		
	chain = []
	j += 1

print max_chain
print getMin(max_chain)

