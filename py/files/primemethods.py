#!/bin/sh

# prime methods.py
# ProjectEuler
#
# Created by joe yuan on 3/8/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

### MY FIRST METHOD

def prime(n):
	"""tests if a nuber is prime or not"""
	t = n - 1
	if n < 2:
		return 0
	elif n == 2 or n == 3:
		return  1
	else:
		for i in range(2,t):
			y = float(n)/i
			if y == int(y):
				check = 0
				break
			else:
				check = 1
		if check == 1:
			return 1
		else:
			return 0

### MY SECOND METHOD, much cleaner =)
def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(n**.5) + 1,2):
        if n%i == 0:
            return False
    return True

# for primes up to f or N
def Sieve(N):
    global x
    x = N*[0]
    for h in range(int(N**.5)+1):
        num = h + 1
        if num >= 2:
            if x[h] == 0:
                for k,c in enumerate(x[num:]):
                    if (k+1)%num == 0:
                            x[k+num] += 1
        else:
            x[h] += 1
    return [j+1 for j,i in enumerate(x) if i == 0]



def Sieve(N):
    x = N*[0]
    for i in range(1,int(N**.5) + 1):
        a = 1
        while i*a < N:
            x[(i*a)-1] += 1
            a += 1
            
    return [j+1 for j,i in enumerate(x) if i == 0]


def prime(f):
    if f < 2:
        print f, "is less than 2 and 2 is the lowest prime number"
        return []
    prime = [2]
    for i in range(3,f,2):
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u: 
            prime.append(i)
    return prime



# for prime factorization
def prime(f):
    prime = [2]
    for i in range(3,int(f**.5),2):###<----modify to range(3,f) for primes up to f
        for c in prime:
            if i%c == 0:
                u = False
                break
            u = True
        if u and f%i == 0: 
            prime.append(i)
    return prime

### for f number of PRIMES

def prime(f):
    prime = [2]
    y = 1003
    while len(prime) != f: #<----n number of primes
        for i in range(y-1000,y): #<---- indent everything below 
            if i%1000 == 0:
                print i, len(prime)
            for c in prime:
                if i%c == 0:
                    u = False
                    break
                u = True
            if u: 
                prime.append(i)
            if len(prime) == f:
                break
        y = y + 1000
    return prime


## FULL PRIME FACTORIZATION OF A NUMBER 
## with exponent count
## in form [primefactor,exponent] 
def primefactor(f):
    factors = [2]
    for i in range(3,int(f**.5),2):
        for c in factors:
            if i%c == 0:
                u = False
                break
            u = True
        if u and f%i == 0: 
            factors.append(i)
    pf = []
    for c in factors:
        g = 0
        for i in range(1,10000):
            if f%(c**i) != 0:
                pf.append([c,g])
                break
            else:
                g = i
    if pf[0][1] == 0:
        pf.pop(0)
    if len(pf) == 0:
        pf.append([f,1])
    return pf