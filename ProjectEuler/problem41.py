
def gen_primes(limit):
	nums = [1] * (limit+1)
	nums[0] = 0
	nums[1] = 0
	for i,x in enumerate(nums):
		if x:
			for k in range(i+i,len(nums),i):
				nums[k] = 0
	return list([i for i,n in enumerate(nums) if n])

primes = gen_primes(10000000)

def is_pandigital(t,n):
	digits = list(range(1,n+1))
	t = str(t)
	for i in t:
		if int(i) in digits:
			digits.remove(int(i))
		else:
			return False
	return True


pan_primes = [x for x in primes if is_pandigital(x,len(str(x)))]

print(pan_primes)
print(pan_primes[-1])