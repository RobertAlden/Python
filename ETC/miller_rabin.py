primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
def miller_rabin(n,tests):
	k = n-1
	r = 0
	while (k % 2 == 0):
		k //= 2
		r += 1
	for t in tests:
		x = pow(t,k,n)
		if x in [1,n-1]:
			continue
		for i in range(r-1):
			x = pow(x,2,n)
			#print(x)
			if x == n-1:
				break
		else:
			return False
	return True

print(sum(primes + [i for i in range(2,2000000) if miller_rabin(i,primes)]))