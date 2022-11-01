import math

limit = 20161

def abundance(n):
	divisors = [] 
	for i in range(1,math.ceil(math.sqrt(n))+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)
	divisors = set(divisors)
	if sum(divisors)-n > n:
		return True

abundant_numbers = []
for i in range(2,limit+1):
	if abundance(i):
		abundant_numbers.append(i)

#print(abundant_numbers)
exceptions = [True]*(limit+1)

for i in abundant_numbers:
	for k in abundant_numbers:
		if i + k <= limit:
			exceptions[i+k] = False
		else:
			break

value = 0
for index,state in enumerate(exceptions):
	if state:
		value += index

print(value,value - 4179871)