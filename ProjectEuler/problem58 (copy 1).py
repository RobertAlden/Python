from math import sqrt

iterations = 30000


def is_prime(n):
	if n < 2:
		return False
	for i in range(2,int(sqrt(n))+1):
		if n % i == 0:
			return False
		i += 1
	else:
		return True


primes = 0
for i in range(1,iterations):
	side_length = 2 * i + 1
	max_value = side_length * side_length
	corners = [max_value-(side_length-1),max_value-(side_length-1)*2,max_value-(side_length-1)*3]
	for c in corners:
		primes += int(is_prime(c))
	if primes / (i*4 + 1) < 0.1:
		print(side_length)
		break
