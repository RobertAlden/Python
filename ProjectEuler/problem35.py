import math
from bisect import bisect_right
def rotate(n):
	n_str = str(n)
	temp = n_str[0]
	n_str = list(n_str)
	for i in range(len(n_str)-1):
		n_str[i] = n_str[i+1]
	n_str[len(n_str)-1] = temp
	n_str = "".join(n_str)
	n_str.join(temp)
	#print(int(n_str))
	return int(n_str)

def is_prime(num):
	if num > 3:
		for i in range(2,int(math.sqrt(num)+1)):
			if (num % i) == 0:
				return False
		else:
			return True
	else:
		if num > 1:
			return True
		else:
			return False

def BinarySearch(a, x): 
    i = bisect_right(a, x) 
    if i != len(a)+1 and a[i-1] == x: 
        return True
    else: 
        return False


limit = 1000001
primes = []
primes.append(0)
for i in range(1,limit):
	primes.append(1)
for i in range(2,int(math.sqrt(limit))):
	if primes[i]:
		coef = 0
		j = i**2
		for j in range(i**2,limit,i):
			primes[j] = 0

primes[0] = 0

numbers = list()	
for i in range(len(primes)):
	if primes[i]:
		numbers.append(i)

numbers.remove(1)
#print(numbers)

i = 0
while i < len(numbers):
	n_str = str(numbers[i])
	for k in n_str:
		if int(k) == 0:
			numbers.remove(numbers[i])
			i-=1
			break
	i+=1


total = 0
i = 0
while i < len(numbers):
	print(len(numbers))
	size = len(str(numbers[i]))
	number = numbers[i]
	fail = 0
	for n in range(size*2):
		number = rotate(number)
		if not BinarySearch(numbers,number):
			fail = 1
			break
	if fail == 1:
		numbers.remove(numbers[i])
		for n in range(size*2):
			number = rotate(number)
			if BinarySearch(numbers,number):
				numbers.remove(number)
		i-=1
	i+=1;

		



print(numbers)
print(len(numbers))