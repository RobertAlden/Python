def Factorial(n):
	res = 1
	for i in range(1,n+1):
		res *= i

	return res

values = []

for i in range(3,500000):
	digits = list(str(i))
	summation = 0
	for n in digits:
		summation += Factorial(int(n))
		if summation > i:
			break
	else:
		if summation == i:
			values.append(i)


print(values)
print(sum(values))