import itertools

permutations = list(map("".join, itertools.permutations('0123456789')))

permutations = [x for x in permutations if x[0] != '0']
results = []

primes = [2,3,5,7,11,13,17]
for n in permutations:
	for t in range(len(n)-3):
		check = n[t+1] + n[t+2] + n[t+3]
		if int(check) % primes[t] != 0:
			break
	else:
		results.append(int(n))

#print(permutations)
print(results)
print(sum(results))