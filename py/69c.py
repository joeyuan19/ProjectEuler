def sieve(N):
    s = [1,1,0]+[0,1]*N
    for i in range(3,int(N**.5)+1,2):
        itr = i*2
        while itr < N:
            s[itr] += 1
            itr += i
    return [i for i in range(N) if s[i] == 0]


def factor(n,sieve):
    temp = []
    for j in sieve:
        if n%j == 0:
            temp.append(j)
        if j > n/2:
            break
    return [1] + temp + [n]

N = 1000000
s = sieve(N)
print "sieve done"
nums = {}
m = -1
mn = -1
for i in range(1,N+1):
    print i,m,mn,
    nums[i] = factor(i,s)
    if i == 1:
        continue
    r = float(i)/len([j for j in range(1,i) if 1 == max(set(nums[i]).intersection(set(nums[j])))])
    print r
    if r > m:
        m = r
        mn = i
     
print "m:",m
print "mn:",mn


print max([(float(num)/len([i for i in range(1,num) if 1 == max(set(nums[num]).intersection(set(nums[i])))]),num)   for num in nums if num != 1])


