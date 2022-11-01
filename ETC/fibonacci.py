from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


fib_seq = [fibonacci(i) for i in range(2,90)]
print(sum(fib_seq))