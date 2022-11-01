def collatz(n):
	if n%2 == 0:
		return n/2
	else:
		return (3*n)+1

largest = 0
largestn = 0
for i in range(1,1000000):
	print(i)
	count = 1
	n = i
	while n != 1:
		n = collatz(n)
		count+=1
	if count > largest:
		largest = count
		largestn = i
print(largestn,largest)