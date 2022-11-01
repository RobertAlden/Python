from math import sqrt
from time import perf_counter

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def is_prime_sqrt(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True

def slow_prime_list(limit):
    primes = []
    for i in range(2,limit):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_list(limit): # Sieve of Eratosthenes
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i,k in enumerate(primes):
        if k:
            for p in range(i+i,limit,i):
                primes[p] = False
    return [i for i,k in enumerate(primes) if k]

check_limit = 10001

tic = perf_counter()
prime_list(check_limit)
toc = perf_counter()
print(f"It took {toc - tic:0.4f} seconds")

tic = perf_counter()
slow_prime_list(check_limit)
toc = perf_counter()
print(f"It took {toc - tic:0.4f} seconds")