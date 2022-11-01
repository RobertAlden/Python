import math

limit = 10000
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


results = []

for i in primes:
	for k in range(int(math.sqrt(limit))+1):
		num = i+2*(k**2)
		if num < limit:
			results.append(num)


numbers = range(1,limit)

numbers = [i for i in numbers if i not in results and i % 2 != 0 and i != 1]
print(numbers)