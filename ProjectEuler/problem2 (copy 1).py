a,b,c = 0,1,0
while b < 4000000:
	a,b = b,a+b
	if (b % 2 == 0):
		c += b
print(c)

numbers = [x for x in range(100)]
print(numbers)

odds = numbers[45:60]
print(odds)