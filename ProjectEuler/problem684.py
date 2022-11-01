from functools import lru_cache
from time import perf_counter

@lru_cache(maxsize=None)
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


fib_seq = [fibonacci(i) for i in range(2,91)]
print(fib_seq)

def s(n):
	a = n // 9
	b = n % 9
	output = str(b) + "".join(["9"]*a)
	return int(output)

def S(k):
	output = 0
	for i in range(1,k+1):
		output += s(i)
	return output


def time_func(f,args,iters=1000):
	t = 0
	for i in range(iters):
		start = perf_counter()
		f(args)
		end = perf_counter()
		t += (end-start)
	print(f"Times: s1:{t/iters}")

k = 0
for i in range(2,91):
	p = S(fib_seq[i])
	print(f"{i}")
	k += p


print(k % 1000000007)