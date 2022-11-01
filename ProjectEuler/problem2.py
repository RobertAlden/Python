def fibonacci(a,b):
	return a+b

limit = 4000000

values = [1,2]

while values[-1] < limit:
	values.append(fibonacci(values[-2],values[-1]))
	print(values)

s = 0

for i in values:
	if i % 2 == 0:
		s += i

print(s)

