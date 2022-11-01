import math

limit = 1000000
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
start = 0
end = 0
while (sum(primes[start:end+1]) < limit):
	end += 1
end -= 1
longest = end

results = []
dist = longest

result = sum(primes[start:end +1])
while (True):
	if result > limit:
		start = 0
		if dist > 1:
			dist -= 1
		else:
			break
	result = sum(primes[start:start+dist + 1])
	if result in primes:
		results.append((result,dist+1))
		print(result,primes[start:start+dist + 1])
		break
	start += 1
print(max(results,key=lambda item:item[1]))