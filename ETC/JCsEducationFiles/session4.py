# total = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)

def sumn(x,r):
    r //= x
    return r * (r+1) * x // 2
limit = 100000000000000000
print(sumn(3,limit-1)+sumn(5,limit-1)-sumn(15,limit-1))

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
for i in range(1,iterations):
    side_length = 2 * i + 1
    max_value = side_length**2
    corners = [max_value-(side_length-1),max_value-(side_length-1)*2,max_value-(side_length-1)*3]
    for c in corners:
        primes += is_prime(c)

    if primes / (4*i + 1) < 0.1:
        print(side_length)
        break

