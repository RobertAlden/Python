import math

limit = 200000
primes = []
primes.append(0)
for i in range(1,limit):
	primes.append(1)
for i in range(2,int(math.sqrt(limit))+1):
	if primes[i]:
		coef = 0
		j = i**2
		for j in range(i**2,limit,i):
			primes[j] = 0

new_primes = [i for (i,j) in enumerate(primes) if j != 0]
del new_primes[0]
primes = new_primes

def factorize(n):
	factors = []
	while n > 1:
		for i in primes:
			#print(n,i)
			if n in primes:
				if n not in factors:
					factors.append(n)
				n = int(n / n)
				break
			elif n % i == 0:
				if i not in factors:
					factors.append(i)
				n = int(n / i)
				break
	return factors


#print(factorize(644))
length = 4
count = 0
for i in range(100000,limit):
	fact = factorize(i)
	if len(fact) == length:
		print(i)
		count+=1
		if count == length:
			for k in range(length,0,-1):
				print(i-k+1)
			break
	else:
		count = 0
