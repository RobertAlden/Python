primes = [2,3,5,7,11,13,17,19]
n = 20
result = 1
for i in primes:
	k = 0
	while (pow(i,k+1)<=n):
		k+=1
	print(i,"^",k)
	result*=pow(i,k)
print(result)