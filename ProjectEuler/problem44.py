import math

def isPentagonal(x):
  r = math.sqrt(1 + 24 * x)
  return r % 6 == 5;

pentas = []

c = 1
i = 1
while c < 25000000:
	if c not in pentas:
		pentas.append(c)
	i+=3
	c+=i

print(pentas)
results = [] 
for i in range(1,5000):
	pi =  i *(3 * i - 1) / 2;
	for j in range(1,5000):
		pj =  j *(3 * j - 1) / 2

		if isPentagonal(abs(pi-pj)) and  isPentagonal(pi+pj):
			results.append((pi,pj,abs(pi-pj)))

print(results)
