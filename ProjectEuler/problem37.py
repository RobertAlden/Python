limit = 800000

def create_primes(limit):
	numbers = [1] * (limit+1)
	numbers.insert(0,0)
	numbers.insert(0,0)
	for x,i in enumerate(numbers):
		if i:
			for k in range(x+x,len(numbers),x):
				numbers[k] = 0
	primes = [i for i,p in enumerate(numbers) if p]
	return primes

def extend_primes(p,limit):
	numbers = p + list(range((p[-1])+1,limit+1))
	primes = []
	while len(numbers):
		primes.append(numbers[0])
		print(len(numbers))
		numbers = [x for x in numbers if x % numbers[0] != 0]
	return primes

primes = create_primes(limit)
truncated = []
filtered_primes = [i for i in primes if len(str(i)) > 1 if int(str(i)[0]) in primes if int(str(i)[-1]) in primes]

print(primes)

while len(truncated) < 11:
	for i in filtered_primes:
		if i not in truncated:
			s = str(i)
			left = False
			right = False
			while len(s):
				if int(s) not in primes:
					break
				else:
					s = s[1:]
			else:
				left = True

			s = str(i)
			while len(s):
				if int(s) not in primes:
					break
				else:
					s = s[:-1]
			else:
				right = True

			if left and right:
				truncated.append(i)
				print(i)
	#primes = extend_primes(primes,limit * 10)
	#filtered_primes = [i for i in primes if len(str(i)) > 1 if int(str(i)[0]) in primes if int(str(i)[-1]) in primes]
	#limit *= 10
	#print(limit)

print(truncated,len(truncated),sum(truncated))
