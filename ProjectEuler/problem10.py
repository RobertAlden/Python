import math

limit = 2000000
primes = []
primes.append(0)
for i in range(1,limit):
	primes.append(1)
for i in range(2,int(math.sqrt(limit))):
	if primes[i]:
		coef = 0
		j = i**2
		for j in range(i**2,limit,i):
			primes[j] = 0
			

summation = 0

for i in range(2,len(primes)):
	if primes[i]:
		print(i)
		summation += i

print(summation)