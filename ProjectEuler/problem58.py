from math import sqrt

def is_prime(n):
    for i in range(2,round(sqrt(n))+1):
        #print(i)
        if n % i == 0:
            return False
    else:
        return True

iterations = 30000
primes = 0
for k in range(1,iterations):
    v = (2 * k) + 1
    max_value = v**2
    corners = [max_value-(v-1)*3,max_value-(v-1)*2,max_value-(v-1)*1]
    for x in corners:
        primes += int(is_prime(x))


    #print(v,corners, (primes / (4 * k + 1)))
    if (primes / (4*k + 1)) < 0.1:
        print(v)
        break
