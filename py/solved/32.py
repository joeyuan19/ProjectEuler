def pancheck(s):
	s = str(s)
	if len(s) != 9:
		return False
	if '1' not in s:
		return False 
	if '2' not in s:
		return False 
	if '3' not in s:
		return False 
	if '4' not in s:
		return False 
	if '5' not in s:
		return False 
	if '6' not in s:
		return False 
	if '7' not in s:
		return False 
	if '8' not in s:
		return False 
	if '9' not in s:
		return False 
	return True

prod = []

a = 1
b = 1
c = 1

t = 123456789
print pancheck(t)

N = 10000

while len(str(a)) < 10:
	c = a*b
	if pancheck(str(a) + str(b) + str(c)):
		if c not in prod:
			prod.append(c)	
		print a, b, c, len(prod) 
	if len(str(a) + str(b) + str(c)) > 9:
		a += 1
		b = a
	elif len(str(a) + str(b)) >= 10:
		break
	else:
		b += 1		
	if a > 100000: break

print sum(prod)

