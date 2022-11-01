import math

number = 600851475143

primes = [False,False]

for i in range(2,int(math.sqrt(number+1))):
	primes.append(True)

for i in range(2,len(primes)):
	if primes[i]:
		for p in range(i+i,len(primes),i):
			primes[p] = False

for i,p in enumerate(primes):
	if p and number % i == 0:
		print(i)
	