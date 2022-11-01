from math import sqrt

def is_prime(n):
    for i in range(2,round(sqrt(n))+1):
        #print(i)
        if n % i == 0:
            return False
    else:
        return True

print(is_prime(13))

def list_of_primes(n):
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return primes

def fast_list_of_primes(n):
    limit = n
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i,k in enumerate(primes):
        if k:
            for p in range(i+i,limit,i):
                primes[p] = False
    return [i for i,k in enumerate(primes) if k]

#print(list_of_primes(100000000000))
print(fast_list_of_primes(1000000))

