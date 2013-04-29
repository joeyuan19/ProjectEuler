"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""

def num(x):
	s = ""
	temp = x
	while temp >= 1000:
		temp = temp - 1000
		s += "M"
	if temp >= 900:
		temp = temp - 900
		s += "CM"
	if temp >= 500:
		temp = temp - 500
		s += "D"
	if temp >= 400:
		temp = temp - 400
		s += "CD"
	while temp >= 100:
		temp = temp - 100
		s += "C"
	if temp >= 90:
		temp = temp - 90
		s += "XC"
	if temp >= 50:
		temp = temp - 50
		s += "L"
	if temp >= 40:
		temp = temp - 40
		s += "XL"
	while temp >= 10:
		temp = temp - 10
		s += "X"
	if temp == 9:
		s += "IX"
		return s
	if temp >= 5:
		temp = temp - 5
		s += "V"
	if temp == 4:
		s += "IV"
		return s
	while temp > 0:
		temp = temp - 1
		s += "I"
	return s

def denum(s):
	x = 0
	length = len(s)
	i = 0
	while i < length:
		if s[i] == "M":
			x += 1000
		if s[i] == "D":
			x += 500
		if s[i] == "C":
			if i != length - 1:
				if s[i+1] == "M":
					x += 900
					i += 1
				elif s[i+1] == "D":
					x += 400
					i += 1
				else:
					x += 100
			else:
				x += 100
		elif s[i] == "L":
			x += 50
		elif s[i] == "X":
			if i != length - 1:
				if s[i+1] == "C":
					x += 90
					i += 1
				elif s[i+1] == "L":
					x += 40
					i += 1
				else:
					x += 10			
			else:
				x += 10
		elif s[i] == "V":
			x += 5
		elif s[i] == "I":
			if i != (len(s) - 1):
				if s[i+1] == "X":
					x += 9
					return x
				elif s[i+1] == "V":
					x += 4
					return x
				else:
					x += 1
			else:
				x += 1
		i += 1
	return x

print 40, num(40), denum("XL")
print 911, num(911), denum("CXVVI")
print 129, num(129), denum("CXXIX")
print 7, num(7), denum("VII")
print 9, num(9), denum("IX")
print 34, num(34), denum("XXXIV")


with open('roman.txt','r') as f:
	nums = [line.strip() for line in f]

orig_len = 0
abrv_len = 0

for i in nums:
	#print i, num(denum(i))
	orig_len += len(i)
	abrv_len += len(num(denum(i)))

print orig_len, abrv_len, (orig_len - abrv_len)

