import math

def GenPrimes(limit):
	primes = []
	for i in range(2,int(math.sqrt(limit+1))):
		primes.append(True)

	for i in range(2,len(primes)):
		if primes[i]:
			for p in range(i+i,len(primes),i):
				primes[p] = False
	return primes

primes_list = GenPrimes(1000000000)

outputs = []
highest = 0
for a in range(-999,1000):
	for b in range(-1000,1001):
		n = 0
		while(True):
			value = n**2 + a * n + b
			if not primes_list[value]:
				if n > highest:
					outputs.append((a*b,n))
					highest = n
				break
			else:
				n+=1

print(outputs)
