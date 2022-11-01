from math import sqrt

X = 600851475143
primes = [True for i in range(round(sqrt(X)+1))]

primes[0] = False
primes[1] = False

for ind,val in enumerate(primes):
	if val:
		for i in range(ind+ind,len(primes),ind):
			primes[i] = False

primes = [i for i,x in enumerate(primes) if x]

factors = []
while X > 1:
	for p in primes:
		if X % p == 0:
			X /= p
			factors += [p]

print(primes)
print(factors)
