import math
triangles = []

triangles.append(0)
for i in range(1,1000000):
	triangles.append(i+triangles[i-1])

for i in triangles:

	divisors = []
	for k in range(2,round(math.sqrt(i))):
		if i % k == 0:
			divisors.append(k)
			divisors.append(i/k)

	if len(divisors)+2 >= 500:
		print(i,divisors)
		break

print("None found.")