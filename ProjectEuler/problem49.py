import math

limit = 10000
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

new_primes = [i for (i,j) in enumerate(primes) if j != 0]
del new_primes[0]
new_primes = [i for i in new_primes if i > 1000]


#print(primes)
print(new_primes)

def is_perm(s,t):
	new_t = str(t)
	new_s = str(s)
	for i in new_t:
		if i not in new_s:
			return False
		new_s = new_s.replace(i,"",1)
	else:
		return len(new_s) == 0

primes = new_primes


for i in primes:
	n = 1
	while n < 5000:
		j = i + n
		k = j + n
		if j in primes and k in primes:
			if is_perm(i,j) and is_perm(i,k):
				print(i,j,k,n)
		n+=1
	
print("DONE")
	