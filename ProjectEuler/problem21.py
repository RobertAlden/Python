import math
def div(n):
	i = n
	divisors = []
	divisors.append(1)
	for k in range(2,round(math.sqrt(i))):
		if i % k == 0:
			divisors.append(int(k))
			divisors.append(int(i/k))
	return divisors

def d(n):
	t = div(n)
	return sum(t)

final = []
for k in range(0,10000):
	p = d(k)
	if d(p) == k and p != k:
		if k not in final:
			final.append(k)
		if p not in final:
			final.append(p)

print(sum(final))