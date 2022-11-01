import math

number = 600851475143

primes = []
tested = []

for i in range(2,int(math.sqrt(number+1))):
	if i not in tested:
		for k in tested:
			if i % k == 0:
				break
		else:
			primes.append(i)
	for p in range(i,int(math.sqrt(number+1)),i):		
		tested.append(p)
	

print(primes)

primes.reverse()

for n in primes:
	if number % n == 0:
		print(n)